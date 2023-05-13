import json
from cv2 import waitKey
from perfectparking import ParkingMonitorData, RestApiUtility
from requests import request
import logging
import random
import time

def main():
    """Main function"""
    logging.basicConfig(level=logging.INFO)

    # Initialize the mock data array with five mock config files
    parking_monitor_data_mocks:list(ParkingMonitorData) =[]
    for number in range(1, 5):
        parking_monitor_data_mocks.append(ParkingMonitorData(f"PerfectParkingClient/mock-{number}-config.ini"))

    while True: # Infinite loop with Key press option to stop
        for mock_parking_monitor_data in parking_monitor_data_mocks:
            send_mock_put_request(mock_parking_monitor_data)
            time.sleep(get_random_seconds_time_delay())


        ###
        # Option to stop the program
        key = waitKey(1)
        was_stopped = key == ord("q")
        if was_stopped:
            return True
        ###

def get_random_seconds_time_delay()->int:
    """Returns a random number of seconds between 1 and 59
    Returns:
        int: Returns a random number of seconds between 1 and 59
    """    
    seconds:int = random.randint(1, 59)
    print(f"Wait for {seconds} seconds")
    return seconds

def send_mock_put_request(parking_monitor_data:ParkingMonitorData):
    """Sends a mock PUT request to the server with random data

    Args:
        parking_monitor_data (ParkingMonitorData): The ParkingMonitorData object to send the PUT request with
    """
    logging.info(f"Sending Mock Data for : {parking_monitor_data.name}")
    parking_spaces:int = int(parking_monitor_data.parking_spaces)
    free_spaces_in_frame:int = random.randint(0, parking_spaces)
    probability_parking_available:float = free_spaces_in_frame / parking_spaces
    response: request.Response = RestApiUtility.update_server_parking_monitor_data(
        parking_monitor_data, free_spaces_in_frame, probability_parking_available
    )
    print(json.dumps(response.json(), indent=4))
    logging.info(f"Response: {response.status_code} {response.reason}")


if __name__ == '__main__':
    main()
