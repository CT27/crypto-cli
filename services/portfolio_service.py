import json
from contextlib import contextmanager
from sqlalchemy.exc import IntegrityError
from rich.console import Console
from models import SessionLocal, User, Portfolio, Cryptocurrency

console = Console()

@contextmanager
def get_session():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        console.log(f"[red]Session rollback due to exception: {e}[/red]")
        raise
    finally:
        session.close()

class PortfolioService:
    PORTFOLIO_FILE = "portfolio.json"

    @staticmethod
    def add_to_portfolio(username, symbol, quantity):
        """
        Adds a cryptocurrency to the user's portfolio.

        Args:
            username (str): The user's username.
            symbol (str): The cryptocurrency symbol (e.g., BTC).
            quantity (float): Amount of cryptocurrency to add.

        Returns:
            str: Success or error message.
        """
        symbol = symbol.upper()  # Normalize symbol to uppercase

        with get_session() as session:
            # Debug: Print all cryptos to verify if symbol exists
            cryptos = session.query(Cryptocurrency).all()
            console.print(f"DEBUG: Cryptos in database: {[(crypto.name, crypto.symbol) for crypto in cryptos]}")

            # Check if user exists
            user = session.query(User).filter_by(username=username).first()
            if not user:
                return f"[bold red]Error: User '{username}' not found.[/bold red]"

            # Check if cryptocurrency exists
            crypto = session.query(Cryptocurrency).filter_by(symbol=symbol).first()
            if not crypto:
                return f"[bold red]Error: Cryptocurrency '{symbol}' not found.[/bold red]"

            try:
                # Check if the portfolio entry already exists
                portfolio = session.query(Portfolio).filter_by(user_id=user.id, crypto_id=crypto.id).first()
                if portfolio:
                    portfolio.quantity += quantity  # Update existing entry
                else:
                    portfolio = Portfolio(user_id=user.id, crypto_id=crypto.id, quantity=quantity)
                    session.add(portfolio)
            except IntegrityError as e:
                console.log(f"[red]IntegrityError: {e}[/red]")
                return "[bold red]Error: Could not add to portfolio due to an integrity error.[/bold red]"

        # Save backup after the transaction
        PortfolioService.save_portfolio_to_json()
        return f"[bold green]Successfully added {quantity} {symbol} to {username}'s portfolio.[/bold green]"

    @staticmethod
    def view_user_portfolio(username):
        """
        Fetches and displays a user's cryptocurrency portfolio.

        Args:
            username (str): The user's username.

        Returns:
            str: Portfolio details or an error message.
        """
        with get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if not user:
                return f"[bold red]Error: User '{username}' not found.[/bold red]"

            portfolios = session.query(Portfolio).filter_by(user_id=user.id).all()
            if not portfolios:
                return f"[bold red]User '{username}' has no cryptocurrencies in their portfolio.[/bold red]"

            portfolio_output = f"[bold cyan]Portfolio for {username}:[/bold cyan]\n"
            for portfolio in portfolios:
                crypto = session.query(Cryptocurrency).filter_by(id=portfolio.crypto_id).first()
                if crypto:
                    portfolio_output += f" - {crypto.name} ({crypto.symbol}): {portfolio.quantity} units\n"
                else:
                    portfolio_output += f" - [red]Unknown Crypto (ID: {portfolio.crypto_id})[/red]: {portfolio.quantity} units\n"
            return portfolio_output

    @staticmethod
    def list_all_portfolios():
        """
        Retrieves all users' portfolios and displays them in a structured format.

        Returns:
            str: A formatted list of all users and their cryptocurrency holdings.
        """
        output = "[bold green]All User Portfolios:[/bold green]\n"
        with get_session() as session:
            users = session.query(User).all()
            if not users:
                return "[bold red]No users found in the database.[/bold red]"

            for user in users:
                portfolios = session.query(Portfolio).filter_by(user_id=user.id).all()
                if portfolios:
                    output += f"\n[bold cyan]{user.username}'s Portfolio:[/bold cyan]\n"
                    for portfolio in portfolios:
                        crypto = session.query(Cryptocurrency).filter_by(id=portfolio.crypto_id).first()
                        if crypto:
                            output += f" - {crypto.name} ({crypto.symbol}): {portfolio.quantity} units\n"
                        else:
                            output += f" - [red]Unknown Crypto (ID: {portfolio.crypto_id})[/red]: {portfolio.quantity} units\n"
                else:
                    output += f"\n[bold cyan]{user.username} has no cryptocurrencies in their portfolio.[/bold cyan]\n"
        return output

    @staticmethod
    def save_portfolio_to_json():
        """
        Saves all user portfolios to a JSON file for backup.
        """
        portfolios_data = {}
        with get_session() as session:
            users = session.query(User).all()
            for user in users:
                portfolios = session.query(Portfolio).filter_by(user_id=user.id).all()
                if portfolios:
                    user_portfolio = {}
                    for portfolio in portfolios:
                        crypto = session.query(Cryptocurrency).filter_by(id=portfolio.crypto_id).first()
                        if crypto:
                            user_portfolio[crypto.symbol] = portfolio.quantity
                    if user_portfolio:
                        portfolios_data[user.username] = user_portfolio

        try:
            with open(PortfolioService.PORTFOLIO_FILE, "w") as f:
                json.dump(portfolios_data, f, indent=4)
        except IOError as e:
            console.log(f"[red]IOError while saving portfolio backup: {e}[/red]")

    @staticmethod
    def load_portfolio_from_json():
        """
        Loads the portfolio backup from JSON.

        Returns:
            dict: A dictionary of user portfolios if found, otherwise empty.
        """
        try:
            with open(PortfolioService.PORTFOLIO_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            console.log(f"[red]Error loading portfolio backup: {e}[/red]")
            return {}

    @staticmethod
    def list_cryptocurrencies():
        """
        Retrieves all available cryptocurrencies from the database.

        Returns:
            list: A list of dictionaries, each representing a cryptocurrency.
        """
        with get_session() as session:
            cryptos = session.query(Cryptocurrency).all()
            # Convert each ORM object to a dictionary to avoid DetachedInstanceError.
            return [
                {"name": crypto.name, "symbol": crypto.symbol, "price": crypto.price}
                for crypto in cryptos
            ]
