from configparser import ConfigParser
from requests.auth import HTTPBasicAuth
import requests


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
        parking_monitor_data_json: dict = RestApiUtility.build_parking_monitor_data_json(
            parking_monitor_data,
            free_spaces_in_frame,
            probability_parking_available)
        return RestApiUtility.build_and_send_parking_monitor_data_put_request(parking_monitor_data, parking_monitor_data_json)

    @staticmethod
    def build_parking_monitor_data_json(parking_monitor_data: ParkingMonitorData, free_spaces_in_frame: float, probability_parking_available: float) -> dict:
        """_summary_

        Args:
            parking_monitor_data (ParkingMonitorData): The parking monitor data to build the json for.
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
            "probabilityParkingAvailable": "{:.2f}".format(probability_parking_available),
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

