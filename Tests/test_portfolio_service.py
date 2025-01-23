import pytest
from models import session, User, Cryptocurrency, Portfolio
from services.portfolio_service import PortfolioService


@pytest.fixture(scope="function", autouse=True)
def cleanup():
    """Clean up the database before each test run."""
    session.query(Portfolio).delete()
    session.query(Cryptocurrency).delete()
    session.query(User).delete()
    session.commit()


def test_add_to_portfolio():
    """Test adding a cryptocurrency to a user's portfolio."""
    user = User(username="johndoe")
    crypto = Cryptocurrency(name="Bitcoin", symbol="BTC", price=50000)
    session.add_all([user, crypto])
    session.commit()

    # Add to portfolio
    result = PortfolioService.add_to_portfolio("johndoe", "BTC", 1.5)
    assert "Successfully added 1.5 BTC to johndoe's portfolio" in result


def test_view_empty_portfolio():
    """Test viewing an empty portfolio for a user."""
    # Ensure user exists before testing portfolio
    user = User(username="johndoe")
    session.add(user)
    session.commit()

    result = PortfolioService.view_user_portfolio("johndoe")
    assert "User 'johndoe' has no cryptocurrencies in their portfolio." in result


def test_view_portfolio():
    """Test viewing a populated portfolio for a user."""
    user = User(username="johndoe")
    crypto = Cryptocurrency(name="Ethereum", symbol="ETH", price=3000)
    session.add_all([user, crypto])
    session.commit()

    # Add cryptocurrency to portfolio
    PortfolioService.add_to_portfolio("johndoe", "ETH", 3.0)

    # View the portfolio
    result = PortfolioService.view_user_portfolio("johndoe")
    assert "Ethereum (ETH): 3.0 units" in result
