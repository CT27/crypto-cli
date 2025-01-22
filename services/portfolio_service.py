import json
from models import session, User, Portfolio, Cryptocurrency

class PortfolioService:
    PORTFOLIO_FILE = "portfolio.json"

    @staticmethod
    def add_to_portfolio(symbol, quantity):
        portfolio = PortfolioService.load_portfolio()
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        PortfolioService.save_portfolio(portfolio)
        return f"Added {quantity} {symbol.upper()} to portfolio."

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
