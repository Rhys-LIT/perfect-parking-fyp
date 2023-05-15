import os
import sys
import unittest

from requests import request
from PerfectParkingClient.perfectparking import ParkingMonitorData, RestApiUtility

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class RestApiUtilityTestSuite(unittest.TestCase):
    """Rest Api Utility test cases."""


    def test_update_server_parking_monitor_data(self):
        """Test update_server_parking_monitor_data method."""
        parking_monitor_data:ParkingMonitorData = ParkingMonitorData()
        free_spaces_in_frame: float = 3
        probability_parking_available:float = 0.5  # (3/6)
        response: request.Response = RestApiUtility.update_server_parking_monitor_data(
            parking_monitor_data, free_spaces_in_frame, probability_parking_available
        )
        expected_response_status_code = 200
        self.assertEqual(response.status_code, expected_response_status_code)


if __name__ == "__main__":
    unittest.main()
