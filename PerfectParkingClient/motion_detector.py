from colors import COLOR_GREEN, COLOR_WHITE, COLOR_BLUE
from configparser import ConfigParser
from drawing_utils import draw_contours
from json import dump
from requests.auth import HTTPBasicAuth
import cv2 as open_cv
import logging
import numpy as np
import requests
import time

SECONDS_TIME_DELAY = .002 # Lower value means faster processing


class ParkingMonitorData:
    """This class represents the data of a parking monitor"""

    def __init__(self, config_filepath: str = "PerfectParkingClient/config.ini"):
        """Constructor of the ParkingMonitorData class

        Args:
            config_filepath (str, optional): The path to the config file to load the data from. Defaults to "config.ini".
        """
        config_parser: ConfigParser = ConfigParser()

        config_parser.read(config_filepath)

        self.id = config_parser["ParkingLotMonitor"]["Id"]
        self.name = config_parser["ParkingLotMonitor"]["Name"]
        self.latitude = config_parser["ParkingLotMonitor"]["Latitude"]
        self.longitude = config_parser["ParkingLotMonitor"]["Longitude"]

        self.app_token = config_parser["App"]["Token"]
        self.app_username = config_parser["App"]["Username"]
        self.app_password = config_parser["App"]["Password"]
        self.server_url = config_parser["App"]["ServerUrl"]


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
        """_summary_

        Raises:
            CaptureReadError: _description_

        Returns:
            bool: returns True if the video was stopped by a key press, False otherwise
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

        frame_number = 0
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
                    len(statuses), free_spaces_in_frame)# TODO:Fix
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
        probability_parking_available = free_spaces_in_frame/spaces_in_frame
        MotionDetector.update_server_parking_monitor_data(
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

    @staticmethod
    def update_server_parking_monitor_data(parking_monitor_data: ParkingMonitorData, free_spaces_in_frame: float, probability_parking_available: float) -> requests.Response:
        """_summary_

        Args:
            parking_monitor_data (ParkingMonitorData): _description_
            free_spaces_in_frame (float): _description_
            probability_parking_available (float): _description_

        Returns:
            requests.Response: _description_
        """             
        parking_monitor_data_json: dict = MotionDetector.build_parking_monitor_data_json(
            parking_monitor_data,
            free_spaces_in_frame,
            probability_parking_available)
        return MotionDetector.build_and_send_parking_monitor_data_put_request(parking_monitor_data, parking_monitor_data_json)

    @staticmethod
    def build_parking_monitor_data_json(parking_monitor_data: ParkingMonitorData, free_spaces_in_frame: float, probability_parking_available: float) -> dict:
        """_summary_

        Args:
            parking_monitor_data (ParkingMonitorData): _description_
            free_spaces_in_frame (float): _description_
            probability_parking_available (float): _description_

        Returns:
            _type_: _description_
        """
        return {
            "id": parking_monitor_data.id,
            "name": parking_monitor_data.name,
            "latitude": parking_monitor_data.latitude,
            "longitude":  parking_monitor_data.longitude,
            "probabilityParkingAvailable": probability_parking_available,
            # "image": image_base_64_encoded,
            # "free_spaces": free_spaces
        }

    @staticmethod
    def build_and_send_parking_monitor_data_put_request(parking_monitor_data: ParkingMonitorData, request_json: dict) -> requests.Response:
        """_summary_

        Args:
            parking_monitor_data (ParkingMonitorData): _description_
            request_json (dict): _description_

        Returns:
            requests.Response: _description_
        """
        request_headers = {
            "Authorization": f"Token {parking_monitor_data.app_token}",
            "Content-Type": "application/json",
        }
        request_url = f"{parking_monitor_data.server_url}/{parking_monitor_data.id}/"
        return MotionDetector.send_put_request(parking_monitor_data,
                                               request_headers,
                                               request_json,
                                               request_url)

    @staticmethod
    def send_put_request(parking_monitor_data: ParkingMonitorData, request_headers: dict,
                         request_json: dict, request_url: str) -> requests.Response:
        """Send a PUT request to the server and return the response.
        Args:
            parking_monitor_data (ParkingMonitorData): Provides username and password required to build Authorization header
            request_headers (dict): The headers to be sent with the request
            request_json (dict): The json to be sent with the request
            request_url (str): The url to send the request to

        Returns:
            requests.Response: The response from the server
        """

        http_basic_auth = HTTPBasicAuth(parking_monitor_data.app_username,
                                        parking_monitor_data.app_password)
        response = requests.put(request_url,
                                auth=http_basic_auth,
                                headers=request_headers,
                                json=request_json)

        return response


class CaptureReadError(Exception):
    pass
