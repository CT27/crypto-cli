import json

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
