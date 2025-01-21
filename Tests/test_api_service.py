from services.api_service import APIService

def test_get_crypto_price():
    price = APIService.get_crypto_price('bitcoin')
    assert isinstance(price, (int, float))
