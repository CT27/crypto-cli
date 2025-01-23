import pytest
from models import session, User, Cryptocurrency, Portfolio

@pytest.fixture(scope="function", autouse=True)
def cleanup():
    """Cleanup the database before each test run."""
    session.query(Portfolio).delete()
    session.query(Cryptocurrency).delete()
    session.query(User).delete()
    session.commit()

def test_user_creation():
    try:
        # Adding test users
        user1 = User(username="testuser")
        user2 = User(username="johndoe")
        session.add_all([user1, user2])
        session.commit()
    except Exception as e:
        session.rollback()
        pytest.fail(f"Database error: {e}") 

    # Verify users were added
    assert session.query(User).filter_by(username="testuser").first() is not None
    assert session.query(User).filter_by(username="johndoe").first() is not None

def test_cryptocurrency_creation():
    try:
        # Adding sample cryptocurrencies
        btc = Cryptocurrency(name="Bitcoin", symbol="BTC", price=50000)
        eth = Cryptocurrency(name="Ethereum", symbol="ETH", price=3000)
        session.add_all([btc, eth])
        session.commit()
    except Exception as e:
        session.rollback()
        pytest.fail(f"Database error: {e}") 
    
    # Verify cryptocurrencies were added
    assert session.query(Cryptocurrency).filter_by(symbol="BTC").first() is not None
    assert session.query(Cryptocurrency).filter_by(symbol="ETH").first() is not None

def test_portfolio_creation():
    test_user_creation()
    test_cryptocurrency_creation()
    
    user1 = session.query(User).filter_by(username="testuser").first()
    user2 = session.query(User).filter_by(username="johndoe").first()
    btc = session.query(Cryptocurrency).filter_by(symbol="BTC").first()
    eth = session.query(Cryptocurrency).filter_by(symbol="ETH").first()

    assert user1 is not None and user2 is not None, "User retrieval failed."
    assert btc is not None and eth is not None, "Cryptocurrency retrieval failed."

    try:
        # Adding portfolios specific to users
        portfolio1 = Portfolio(user_id=user1.id, crypto_id=btc.id, quantity=2)
        portfolio2 = Portfolio(user_id=user2.id, crypto_id=eth.id, quantity=5)
        session.add_all([portfolio1, portfolio2])
        session.commit()
    except Exception as e:
        session.rollback()
        pytest.fail(f"Database error: {e}") 

    # Verify portfolios were added
    assert session.query(Portfolio).filter_by(user_id=user1.id, crypto_id=btc.id).first() is not None
    assert session.query(Portfolio).filter_by(user_id=user2.id, crypto_id=eth.id).first() is not None

def test_cleanup():
    session.query(Portfolio).delete()
    session.query(Cryptocurrency).delete()
    session.query(User).delete()
    session.commit()
    
    assert session.query(User).count() == 0
    assert session.query(Portfolio).count() == 0
    assert session.query(Cryptocurrency).count() == 0

if __name__ == "__main__":
    pytest.main()
