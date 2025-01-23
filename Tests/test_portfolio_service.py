import pytest
from models import session, User, Cryptocurrency, Portfolio
from services.portfolio_service import PortfolioService

@pytest.fixture(scope="function", autouse=True)
def cleanup():
    session.query(Portfolio).delete()
    session.query(Cryptocurrency).delete()
    session.query(User).delete()
    session.commit()

def test_add_to_portfolio():
    user = User(username="johndoe")
    crypto = Cryptocurrency(name="Bitcoin", symbol="BTC", price=50000)
    session.add_all([user, crypto])
    session.commit()

    result = PortfolioService.add_to_portfolio("johndoe", "BTC", 1.5)
    assert "Successfully added 1.5 BTC to johndoe's portfolio" in result

def test_view_empty_portfolio():
    result = PortfolioService.view_user_portfolio("johndoe")
    assert "User 'johndoe' has no cryptocurrencies in their portfolio." in result

def test_view_portfolio():
    user = User(username="johndoe")
    crypto = Cryptocurrency(name="Ethereum", symbol="ETH", price=3000)
    session.add_all([user, crypto])
    session.commit()

    PortfolioService.add_to_portfolio("johndoe", "ETH", 3.0)
    result = PortfolioService.view_user_portfolio("johndoe")
    assert "Ethereum (ETH): 3.0 units" in result
