import os
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

if os.environ.get("TESTING"):
    # Use an in-memory database when testing.
    DATABASE_URL = "sqlite:///:memory:"
else:
    # Use an absolute path for the production database.
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_PATH = os.path.join(BASE_DIR, "crypto_portfolio.db")
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    portfolios = relationship('Portfolio', back_populates='user')

class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    symbol = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)

class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    crypto_id = Column(Integer, ForeignKey('cryptocurrencies.id'))
    quantity = Column(Float, nullable=False)
    
    user = relationship('User', back_populates='portfolios')
    cryptocurrency = relationship('Cryptocurrency')

# Create the engine using the proper database URL.
engine = create_engine(DATABASE_URL, echo=True)

# Create session factory and a scoped session.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = scoped_session(SessionLocal)

# Create tables if they do not exist.
Base.metadata.create_all(engine)
