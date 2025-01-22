import pytest
from models import session, User, Cryptocurrency, Portfolio

def test_user_creation():
    # Adding test users
    user1 = User(username="testuser")
    user2 = User(username="johndoe")
    session.add_all([user1, user2])
    session.commit()
    
    # Verify users were added
    assert session.query(User).filter_by(username="testuser").first() is not None
    assert session.query(User).filter_by(username="johndoe").first() is not None

def test_cryptocurrency_creation():
    # Adding sample cryptocurrencies
    btc = Cryptocurrency(name="Bitcoin", symbol="BTC", price=50000)
    eth = Cryptocurrency(name="Ethereum", symbol="ETH", price=3000)
    session.add_all([btc, eth])
    session.commit()
    
    # Verify cryptocurrencies were added
    assert session.query(Cryptocurrency).filter_by(symbol="BTC").first() is not None
    assert session.query(Cryptocurrency).filter_by(symbol="ETH").first() is not None

def test_portfolio_creation():
    # Retrieve users and cryptocurrencies
    user1 = session.query(User).filter_by(username="testuser").first()
    user2 = session.query(User).filter_by(username="johndoe").first()
    btc = session.query(Cryptocurrency).filter_by(symbol="BTC").first()
    eth = session.query(Cryptocurrency).filter_by(symbol="ETH").first()

    # Adding portfolios specific to users
    portfolio1 = Portfolio(user_id=user1.id, crypto_id=btc.id, quantity=2)
    portfolio2 = Portfolio(user_id=user2.id, crypto_id=eth.id, quantity=5)
    session.add_all([portfolio1, portfolio2])
    session.commit()

    # Verify portfolios were added
    assert session.query(Portfolio).filter_by(user_id=user1.id, crypto_id=btc.id).first() is not None
    assert session.query(Portfolio).filter_by(user_id=user2.id, crypto_id=eth.id).first() is not None

def test_cleanup():
    # Clean up the test data
    session.query(Portfolio).delete()
    session.query(Cryptocurrency).delete()
    session.query(User).delete()
    session.commit()

if __name__ == "__main__":
    pytest.main()
