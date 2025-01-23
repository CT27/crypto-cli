import json
from models import session, User, Portfolio, Cryptocurrency
from sqlalchemy.exc import IntegrityError

class PortfolioService:
    PORTFOLIO_FILE = "portfolio.json"

    @staticmethod
    def add_to_portfolio(username, symbol, quantity):
        # Check if the user exists
        user = session.query(User).filter_by(username=username).first()
        if not user:
            return f"[bold red]Error: User '{username}' not found.[/bold red]"

        # Check if the cryptocurrency exists
        crypto = session.query(Cryptocurrency).filter_by(symbol=symbol.upper()).first()
        if not crypto:
            return f"[bold red]Error: Cryptocurrency '{symbol}' not found.[/bold red]"

        try:
            # Check if portfolio entry exists
            portfolio = session.query(Portfolio).filter_by(user_id=user.id, crypto_id=crypto.id).first()
            if portfolio:
                portfolio.quantity += quantity  # Update existing portfolio entry
            else:
                portfolio = Portfolio(user_id=user.id, crypto_id=crypto.id, quantity=quantity)
                session.add(portfolio)

            session.commit()
            return f"[bold green]Successfully added {quantity} {symbol.upper()} to {username}'s portfolio.[/bold green]"
        except IntegrityError:
            session.rollback()
            return "[bold red]Error: Could not add to portfolio.[/bold red]"

    @staticmethod
    def view_portfolio():
        portfolio = PortfolioService.load_portfolio()
        if not portfolio:
            return "Your portfolio is empty."
        return portfolio
    
    @staticmethod
    def view_user_portfolio(username):
        user = session.query(User).filter_by(username=username).first()
        if not user:
            return f"[bold red]Error: User '{username}' not found.[/bold red]"

        # Ensure query filters by user_id
        portfolios = session.query(Portfolio).filter(Portfolio.user_id == user.id).all()
        if not portfolios:
            return f"[bold red]User '{username}' has no cryptocurrencies in their portfolio.[/bold red]"

        portfolio_output = f"Portfolio for {username}:\n"
        for portfolio in portfolios:
            crypto = session.query(Cryptocurrency).filter_by(id=portfolio.crypto_id).first()
            portfolio_output += f"{crypto.name} ({crypto.symbol.upper()}): {portfolio.quantity} units\n"
        
        return portfolio_output

    @staticmethod
    def load_portfolio():
        try:
            with open(PortfolioService.PORTFOLIO_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_portfolio(portfolio):
        with open(PortfolioService.PORTFOLIO_FILE, "w") as f:
            json.dump(portfolio, f, indent=4)
