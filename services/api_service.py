import requests

class APIService:
    API_URL = "https://api.coingecko.com/api/v3/simple/price"

    @staticmethod
    def get_crypto_price(symbol, currency="usd"):
        try:
            response = requests.get(APIService.API_URL, params={"ids": symbol.lower(), "vs_currencies": currency})
            data = response.json()
            if symbol.lower() in data:
                return data[symbol.lower()][currency]
            else:
                return None
        except Exception as e:
            return None

    @staticmethod
    def convert_crypto(symbol, amount, target_currency):
        try:
            response = requests.get(APIService.API_URL, params={"ids": symbol.lower(), "vs_currencies": target_currency.lower()})
            data = response.json()
            if symbol.lower() in data:
                rate = data[symbol.lower()][target_currency.lower()]
                return amount * rate
            else:
                return None
        except Exception as e:
            return None