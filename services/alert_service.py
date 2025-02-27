import json
import time
from services.api_service import APIService  # Adjust the import path if necessary
from rich.console import Console

console = Console()

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

    @staticmethod
    def check_alerts_automatically():
        """
        Check current prices for each alert and notify if the target price is reached.
        """
        alerts = AlertService.load_alerts()
        for symbol, target_price in alerts.items():
            current_price = APIService.get_crypto_price(symbol)
            
            print(f"DEBUG: {symbol.upper()} current price is: {current_price}")
            if current_price is not None and current_price >= target_price:
                console.print(
                    f"[bold green]Alert Triggered: {symbol.upper()} has reached ${current_price}! (Threshold: ${target_price})[/bold green]"
                )
                # Optionally, remove or update the alert after triggering
                # alerts.pop(symbol, None)
        # Optionally, save updated alerts if any were removed
        # AlertService.save_alerts(alerts)

    @staticmethod
    def run_price_checker(interval=60):
        """
        Continuously check alerts at a set interval (in seconds).
        """
        while True:
            AlertService.check_alerts_automatically()
            time.sleep(interval)

if __name__ == "__main__":
    # Optionally, you can set a custom interval (in seconds)
    AlertService.run_price_checker(interval=60)
