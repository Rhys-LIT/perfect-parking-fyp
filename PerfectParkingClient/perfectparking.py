"""This module contains the PerfectParking classes and functions."""
from configparser import ConfigParser
from requests.auth import HTTPBasicAuth
import requests
from cv2 import destroyAllWindows, imshow, imwrite, INTER_CUBIC, Mat, resize, VideoCapture, waitKey


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
        self.parking_spaces = config_parser["ParkingLotMonitor"]["ParkingSpaces"]

        self.app_token = config_parser["App"]["Token"]
        self.app_username = config_parser["App"]["Username"]
        self.app_password = config_parser["App"]["Password"]
        self.server_url = config_parser["App"]["ServerUrl"]
        

class RestApiUtility:
    """This class contains utility methods for interacting with the server REST API"""

    @staticmethod
    def update_server_parking_monitor_data(parking_monitor_data: ParkingMonitorData, free_spaces_in_frame: float, probability_parking_available: float) -> requests.Response:
        """
    Updates the parking monitor data on the server with new free spaces and probability data.

    Args:
        parking_monitor_data: A ParkingMonitorData object representing the parking monitor being updated.
        free_spaces_in_frame: A float representing the number of free spaces in the current video frame.
        probability_parking_available: A float representing the probability that a parking spot is available.

    Returns:
        A requests.Response object representing the server's response to the PUT request.

    Raises:
        None
    """
        parking_monitor_data_json: dict = RestApiUtility.build_parking_monitor_data_json(
            parking_monitor_data,
            free_spaces_in_frame,
            probability_parking_available)
        return RestApiUtility.build_and_send_parking_monitor_data_put_request(parking_monitor_data, parking_monitor_data_json)

    @staticmethod
    def build_parking_monitor_data_json(parking_monitor_data: ParkingMonitorData, free_spaces_in_frame: float, probability_parking_available: float) -> dict:
        """ this method builds the json for the parking monitor data

        Args:
            parking_monitor_data (ParkingMonitorData): the parking monitor data
            free_spaces_in_frame (float): the free spaces in the frame
            probability_parking_available (float): the probability that a parking spot is available

        Returns:
            dict: the json for the parking monitor data
        """
        return {
            "id": parking_monitor_data.id,
            "name": parking_monitor_data.name,
            "latitude": parking_monitor_data.latitude,
            "longitude":  parking_monitor_data.longitude,
            "probabilityParkingAvailable": "{:.2f}".format(probability_parking_available),
            # "image": image_base_64_encoded,
            # "free_spaces": free_spaces
        }

    @staticmethod
    def build_and_send_parking_monitor_data_put_request(parking_monitor_data: ParkingMonitorData, request_json: dict) -> requests.Response:
        """Builds and sends a PUT request to the server and returns the response.

        Args:
            parking_monitor_data (ParkingMonitorData): the parking monitor data
            request_json (dict): the json for the request

        Returns:
            requests.Response: the response from the server
        """
        request_headers = {
            "Authorization": f"Token {parking_monitor_data.app_token}",
            "Content-Type": "application/json",
        }
        request_url = f"{parking_monitor_data.server_url}/{parking_monitor_data.id}/"
        return RestApiUtility.send_put_request(parking_monitor_data,
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

def create_image_from_video(image_file_path:str, video_connection_string:str) -> None:
    """ Creates an image file from a video source.

    Args:
        image_file_path (str): The path to save the image file
        video_connection_string (str): The connection string to the video source
    """

    image_dimensions:tuple = (480, 640)

    zoom_factor:float = 1

    display_dimensions:tuple = (int(image_dimensions[0] * zoom_factor),
                                        int(image_dimensions[1] * zoom_factor))

    video_capture:VideoCapture = VideoCapture(video_connection_string)
    window_name:str = "Press 's' to save image"


    while True:
        is_open:bool = False
        video_frame:Mat = None
        is_open, video_frame = video_capture.read()

        if not is_open:
            print("Unable to video connection")
            break

        display_video_frame:Mat = resize(video_frame, display_dimensions, interpolation = INTER_CUBIC)
        imshow(window_name, display_video_frame)

        if waitKey(1) & 0xFF == ord('s'):
            imwrite(image_file_path, video_frame)
            break

    video_capture.release()
    destroyAllWindows()
