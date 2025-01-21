import unittest
from unittest.mock import patch
from services.api_service import APIService

class TestAPIService(unittest.TestCase):

    @patch("services.api_service.requests.get")
    def test_get_crypto_price_success(self, mock_get):
        mock_get.return_value.json.return_value = {
            "bitcoin": {"usd": 45000}
        }
        price = APIService.get_crypto_price("bitcoin")
        self.assertEqual(price, 45000)

    @patch("services.api_service.requests.get")
    def test_get_crypto_price_not_found(self, mock_get):
        mock_get.return_value.json.return_value = {}
        price = APIService.get_crypto_price("unknowncrypto")
        self.assertIsNone(price)

    @patch("services.api_service.requests.get")
    def test_get_crypto_price_api_failure(self, mock_get):
        mock_get.side_effect = Exception("API request failed")
        price = APIService.get_crypto_price("bitcoin")
        self.assertIsNone(price)

    @patch("services.api_service.requests.get")
    def test_convert_crypto_success(self, mock_get):
        mock_get.return_value.json.return_value = {
            "bitcoin": {"eur": 42000}
        }
        converted_value = APIService.convert_crypto("bitcoin", 2, "eur")
        self.assertEqual(converted_value, 84000)

if __name__ == "__main__":
    unittest.main()
