import argparse
import requests
import json
import datetime
from rich.console import Console
from rich.table import Table
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

API_URL = "https://api.coingecko.com/api/v3/simple/price"
console = Console()

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

engine = create_engine('sqlite:///crypto_portfolio.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

PORTFOLIO_FILE = "portfolio.json"

ALERTS_FILE = "alerts.json"

def get_crypto_price(symbol):
    try:
        response = requests.get(API_URL, params={"ids": symbol.lower(), "vs_currencies": "usd"})
        data = response.json()
        if symbol.lower() in data:
            price = data[symbol.lower()]['usd']
            console.print(f"[bold green]{symbol.upper()} Price: ${price}[/bold green]")
        else:
            console.print(f"[bold red]Error: Cryptocurrency '{symbol}' not found.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error fetching data: {e}[/bold red]")

def set_price_alert(symbol, target_price):
    alerts = load_alerts()
    alerts[symbol.lower()] = target_price
    save_alerts(alerts)
    console.print(f"[bold yellow]Alert set for {symbol.upper()} at ${target_price}[/bold yellow]")

def load_alerts():
    try:
        with open(ALERTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_alerts(alerts):
    with open(ALERTS_FILE, "w") as f:
        json.dump(alerts, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Crypto CLI Tool")
    subparsers = parser.add_subparsers(dest='command')

    price_parser = subparsers.add_parser("price", help="Get cryptocurrency price")
    price_parser.add_argument("symbol", type=str, help="Cryptocurrency symbol (e.g. bitcoin, ethereum)")

    alert_parser = subparsers.add_parser("alert", help="Set a price alert")
    alert_parser.add_argument("symbol", type=str, help="Cryptocurrency symbol (e.g. bitcoin)")
    alert_parser.add_argument("target_price", type=float, help="Target price for alert")

    args = parser.parse_args()
    if args.command == "price":
        get_crypto_price(args.symbol)
    elif args.command == "alert":
        set_price_alert(args.symbol, args.target_price)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
