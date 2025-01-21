import json

ALERTS_FILE = "alerts.json"

def set_price_alert(symbol, target_price):
    alerts = load_alerts()
    alerts[symbol.lower()] = target_price
    save_alerts(alerts)

def load_alerts():
    try:
        with open(ALERTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_alerts(alerts):
    with open(ALERTS_FILE, "w") as f:
        json.dump(alerts, f, indent=4)
