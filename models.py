from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    portfolios = relationship('Portfolio', back_populates='user')

class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    symbol = Column(String, unique=True, nullable=False)

class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    crypto_id = Column(Integer, ForeignKey('cryptocurrencies.id'))
    quantity = Column(Float, nullable=False)
    
    user = relationship('User', back_populates='portfolios')
    cryptocurrency = relationship('Cryptocurrency')

# Database connection
DATABASE_URL = "sqlite:///crypto_portfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create session factory
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Ensure tables are created (run this once)
Base.metadata.create_all(engine)
