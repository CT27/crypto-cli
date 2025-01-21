import json

class AlertService:
    ALERTS_FILE = "alerts.json"

    @staticmethod
    def set_alert(symbol, target_price):
        alerts = AlertService.load_alerts()
        alerts[symbol.lower()] = target_price
        AlertService.save_alerts(alerts)
        return f"Alert set for {symbol.upper()} at ${target_price}"

    @staticmethod
    def check_alerts():
        alerts = AlertService.load_alerts()
        return alerts if alerts else "No alerts set."

    @staticmethod
    def load_alerts():
        try:
            with open(AlertService.ALERTS_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_alerts(alerts):
        with open(AlertService.ALERTS_FILE, "w") as f:
            json.dump(alerts, f, indent=4)
