import time
import cv2
import numpy
from colors import COLOR_GREEN, COLOR_WHITE, COLOR_BLUE
from drawing_utils import draw_contours
from cv2 import boundingRect, cvtColor, destroyAllWindows, drawContours, GaussianBlur, imshow, Laplacian, Mat, VideoCapture
from numpy import ndarray
from perfectparking import ParkingMonitorData, RestApiUtility

SECONDS_TIME_DELAY = .002 # Lower value means faster processing

class ParkingSpot:
    """The ParkingSpot class is responsible for storing the coordinates of a parking spot 
    and the status of the parking spot."""

    def __init__(self, coordinates: ndarray, parking_spot_id: int):
        self.coordinates: ndarray = coordinates
        self.is_occupied: bool = False
        self.parking_spot_id: int = parking_spot_id
        self.rect = boundingRect(self.coordinates)
        self.mask:list = self.create_contours_mask()

    def create_contours_mask(self)->list:
        new_coordinates = self.coordinates.copy()

        x, y, width, height = self.rect
        new_coordinates[:, 0] = self.coordinates[:, 0] - x
        new_coordinates[:, 1] = self.coordinates[:, 1] - y

        contours:list = drawContours(
            numpy.zeros((height, width), dtype=numpy.uint8),
            [new_coordinates],
            contourIdx=-1,
            color=255,
            thickness=-1,
            lineType=cv2.LINE_8)

        contours = contours == 255
        return contours

    def determine_and_mark_occupancy_from_image(self, blurred_grayed_image:Mat):
        """Determines if the parking spot is occupied from the image and marks the parking spot as
        occupied or not occupied."""
        x, y, width, height = self.rect

        parking_spot_image:Mat = blurred_grayed_image[y:(y + height), x:(x + width)]
        laplacian = cv2.Laplacian(parking_spot_image, cv2.CV_64F)

        laplacian_mean: float = numpy.mean(numpy.abs(laplacian * self.mask))
        self.is_occupied = laplacian_mean < MotionDetector.LAPLACIAN_UPPER_LIMIT


    def has_changed(self, is_occupied: bool) -> bool:
        """Checks if the parking occupancy has changed.

        Args:
            is_occupied (bool): True if the parking spot is occupied, False otherwise.

        Returns:
            bool: Returns True if the parking spot occupancy has changed, False otherwise.
        """
        return self.is_occupied != is_occupied

    def has_not_changed(self, is_occupied: bool) -> bool:
        """Checks if the parking occupancy has not changed.

        Args:
            is_occupied (bool): True if the parking spot is occupied, False otherwise.

        Returns:
            bool: Returns True if the parking spot occupancy has not changed, False otherwise.
        """
        return self.is_occupied == is_occupied

        
class MotionDetector:
    """The MotionDetector class is responsible for detecting motion in a video."""
    LAPLACIAN_UPPER_LIMIT = 1.4

    def __init__(self, video, parking_spots_json_dict, start_frame, parking_monitor_data: ParkingMonitorData):
        self.video = video
        self.parking_spots: list = [
            ParkingSpot(numpy.array(parking_spot_json_dict["coordinates"]), parking_spot_json_dict["id"])
            for parking_spot_json_dict in parking_spots_json_dict
        ]

        self.start_frame = start_frame
        self.parking_monitor_data = parking_monitor_data

    def detect_motion(self)->bool:
        """Detects motion in the video and updates the internal state of the MotionDetector object accordingly.
        Raises:
            CaptureReadError: If there is an error reading the video capture.

        Returns:
            bool: True if the video was stopped by a key press, False otherwise.
        """
        video_capture:VideoCapture = VideoCapture(self.video)
        #video_capture:VideoCapture = VideoCapture(0, cv2.CAP_DSHOW)
        #video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame)

        free_spaces: int = 0
        while True:
            is_open:bool = False
            video_frame:Mat = None
            is_open, video_frame = video_capture.read()
            if video_frame is None:
                break

            if not is_open:
                raise CaptureReadError(f"Error reading video capture on frame {video_frame}")

            blurred_image = GaussianBlur(video_frame.copy(), (5, 5), 3)
            blurred_grayed_image: Mat = cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

            for parking_spot in self.parking_spots:
                parking_spot.determine_and_mark_occupancy_from_image(blurred_grayed_image)



            self.display_image(video_frame)

            # Wait 10 seconds and then print the number of empty spaces
            free_spaces_in_frame = len(self.parking_spots) - self.count_occupied_parking_spaces()
            if free_spaces != free_spaces_in_frame:
                self.on_free_parking_spaces_changed(
                    len(self.parking_spots), free_spaces_in_frame)
                free_spaces = free_spaces_in_frame

            k = cv2.waitKey(1)

            if k == ord("q"):
                return True
            time.sleep(SECONDS_TIME_DELAY)
        video_capture.release()
        cv2.destroyAllWindows()
        return False

    def display_image(self, video_frame:Mat):
        for parking_spot in self.parking_spots:
            color:tuple = COLOR_GREEN if parking_spot.is_occupied else COLOR_BLUE
            parking_spot_text:str = str(parking_spot.parking_spot_id)
            draw_contours(video_frame, parking_spot.coordinates, parking_spot_text, COLOR_WHITE, color)
        imshow("Press q to quit", video_frame)
    
    def count_occupied_parking_spaces(self) -> int:
        """Counts the number of occupied parking spaces.

        Returns:
            int: The number of occupied parking spaces.
        """
        return sum(1 for parking_spot in self.parking_spots if parking_spot.is_occupied)


    def on_free_parking_spaces_changed(self, spaces_in_frame: int, free_spaces_in_frame: float) -> None:
        """Event handler for when the number of free parking spaces changes.
        Calls the RestApiUtility to update the server with the new data.

        Args:
            spaces_in_frame (int): The total number of parking spaces in the frame
            free_spaces_in_frame (float): The number of free parking spaces in the frame
        """
        probability_parking_available = free_spaces_in_frame/spaces_in_frame
        RestApiUtility.update_server_parking_monitor_data(
            self.parking_monitor_data, free_spaces_in_frame, probability_parking_available)


class CaptureReadError(Exception):
    pass
