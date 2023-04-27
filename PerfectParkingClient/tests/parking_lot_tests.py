import os
import sys
import unittest

from requests import request
from parking_lot.motion_detector import MotionDetector, ParkingMonitorData

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class MotionDetectorTestSuite(unittest.TestCase):
    """MotionDetector test cases."""

    def test_update_server_parking_monitor_data(self):
        """Test update_server_parking_monitor_data method."""        
        parking_monitor_data = ParkingMonitorData()
        free_spaces_in_frame: float = 3
        probability_parking_available: .5 # (3/6)
        response: request.Response = MotionDetector.update_server_parking_monitor_data(parking_monitor_data, free_spaces_in_frame, probability_parking_available)
        expected_response_status_code = 200
        self.assertEqual(response.status_code, expected_response_status_code)



if __name__ == '__main__':
    unittest.main()