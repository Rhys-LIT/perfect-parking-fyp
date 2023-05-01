from perfectparking import ParkingMonitorData, RestApiUtility
from colors import COLOR_GREEN, COLOR_WHITE, COLOR_BLUE
from drawing_utils import draw_contours
import cv2 as open_cv
import logging
import numpy as np
import time

SECONDS_TIME_DELAY = .002 # Lower value means faster processing

class MotionDetector:
    LAPLACIAN = 1.4
    DETECT_DELAY = 1

    def __init__(self, video, coordinates, start_frame, parking_monitor_data: ParkingMonitorData):
        self.video = video
        self.coordinates_data = coordinates
        self.start_frame = start_frame
        self.contours = []
        self.bounds = []
        self.mask = []
        self.parking_monitor_data = parking_monitor_data

    def detect_motion(self)->bool:
        """Detects motion in the video and updates the internal state of the MotionDetector object accordingly.

    Raises:
        CaptureReadError: If there is an error reading the video capture.

    Returns:
        bool: True if the video was stopped by a key press, False otherwise.
    """ 
        
        capture = open_cv.VideoCapture(self.video)
        capture.set(open_cv.CAP_PROP_POS_FRAMES, self.start_frame)

        coordinates_data = self.coordinates_data
        logging.debug("coordinates data: %s", coordinates_data)

        for p in coordinates_data:
            coordinates = self._coordinates(p)
            logging.debug("coordinates: %s", coordinates)

            rect = open_cv.boundingRect(coordinates)
            logging.debug("rect: %s", rect)

            new_coordinates = coordinates.copy()
            new_coordinates[:, 0] = coordinates[:, 0] - rect[0]
            new_coordinates[:, 1] = coordinates[:, 1] - rect[1]
            logging.debug("new_coordinates: %s", new_coordinates)

            self.contours.append(coordinates)
            self.bounds.append(rect)

            mask = open_cv.drawContours(
                np.zeros((rect[3], rect[2]), dtype=np.uint8),
                [new_coordinates],
                contourIdx=-1,
                color=255,
                thickness=-1,
                lineType=open_cv.LINE_8)

            mask = mask == 255
            self.mask.append(mask)
            logging.debug("mask: %s", self.mask)

        statuses = [False] * len(coordinates_data)
        times = [None] * len(coordinates_data)

        free_spaces: int = 0
        while capture.isOpened():
            result, frame = capture.read()
            if frame is None:
                break

            if not result:
                raise CaptureReadError(
                    "Error reading video capture on frame %s" % str(frame))

            blurred = open_cv.GaussianBlur(frame.copy(), (5, 5), 3)
            grayed = open_cv.cvtColor(blurred, open_cv.COLOR_BGR2GRAY)
            new_frame = frame.copy()
            logging.debug("new_frame: %s", new_frame)

            position_in_seconds = capture.get(
                open_cv.CAP_PROP_POS_MSEC) / 1000.0

            for index, c in enumerate(coordinates_data):
                status = self.__apply(grayed, index, c)

                if times[index] is not None and self.same_status(statuses, index, status):
                    times[index] = None
                    continue

                if times[index] is not None and self.status_changed(statuses, index, status):
                    if position_in_seconds - times[index] >= MotionDetector.DETECT_DELAY:
                        statuses[index] = status
                        times[index] = None
                    continue

                if times[index] is None and self.status_changed(statuses, index, status):
                    times[index] = position_in_seconds

            for index, p in enumerate(coordinates_data):
                coordinates = self._coordinates(p)

                color = COLOR_GREEN if statuses[index] else COLOR_BLUE
                draw_contours(new_frame, coordinates, str(
                    p["id"] + 1), COLOR_WHITE, color)

            open_cv.imshow(str(self.video), new_frame)

            # Wait 10 seconds and then print the number of empty spaces
            free_spaces_in_frame = len(statuses) - statuses.count(0)
            if free_spaces != free_spaces_in_frame:
                self.on_free_parking_spaces_changed(
                    len(statuses), free_spaces_in_frame)
                free_spaces = free_spaces_in_frame

            k = open_cv.waitKey(1)

            if k == ord("q"):
                return True
            time.sleep(SECONDS_TIME_DELAY)
        capture.release()
        open_cv.destroyAllWindows()
        return False

    def __apply(self, grayed, index, p):
        coordinates = self._coordinates(p)
        logging.debug("points: %s", coordinates)

        rect = self.bounds[index]
        logging.debug("rect: %s", rect)

        roi_gray = grayed[rect[1]:(rect[1] + rect[3]),
                          rect[0]:(rect[0] + rect[2])]
        laplacian = open_cv.Laplacian(roi_gray, open_cv.CV_64F)
        logging.debug("laplacian: %s", laplacian)

        coordinates[:, 0] = coordinates[:, 0] - rect[0]
        coordinates[:, 1] = coordinates[:, 1] - rect[1]

        status = np.mean(
            np.abs(laplacian * self.mask[index])) < MotionDetector.LAPLACIAN
        logging.debug("status: %s", status)

        return status

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

    @staticmethod
    def _coordinates(p):
        return np.array(p["coordinates"])

    @staticmethod
    def same_status(coordinates_status, index, status):
        return status == coordinates_status[index]

    @staticmethod
    def status_changed(coordinates_status, index, status):
        return status != coordinates_status[index]


class CaptureReadError(Exception):
    pass
