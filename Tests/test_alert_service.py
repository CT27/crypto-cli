import unittest
import os
import json
from services.alert_service import AlertService

class TestAlertService(unittest.TestCase):

    def setUp(self):
        # Create a temporary alert file for testing
        self.test_alert_file = "test_alerts.json"
        AlertService.ALERTS_FILE = self.test_alert_file

    def tearDown(self):
        # Cleanup test file after tests
        if os.path.exists(self.test_alert_file):
            os.remove(self.test_alert_file)

    def test_set_alert(self):
        result = AlertService.set_alert("bitcoin", 50000)
        self.assertEqual(result, "Alert set for BITCOIN at $50000")
        with open(self.test_alert_file, "r") as f:
            data = json.load(f)
        self.assertEqual(data["bitcoin"], 50000)

    def test_check_alerts_no_alerts(self):
        result = AlertService.check_alerts()
        self.assertEqual(result, "No alerts set.")

    def test_check_alerts_triggered(self):
        AlertService.set_alert("bitcoin", 50000)
        AlertService.set_alert("ethereum", 3000)
        alerts = AlertService.check_alerts()
        self.assertIsInstance(alerts, dict)
        self.assertIn("bitcoin", alerts)

    def test_load_alerts_file_not_exist(self):
        os.remove(self.test_alert_file) if os.path.exists(self.test_alert_file) else None
        alerts = AlertService.load_alerts()
        self.assertEqual(alerts, {})

if __name__ == "__main__":
    unittest.main()
