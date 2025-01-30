import click
from rich.console import Console
from services.alert_service import AlertService
from services.api_service import APIService
from services.portfolio_service import PortfolioService
from services.user_service import UserService
from Utils.update_cryptos import fetch_crypto_data, update_cryptocurrencies_table

console = Console()

@click.group()
def cli():
    """Crypto CLI Tool - Manage cryptocurrency data, portfolios, and alerts."""
    pass

# ✅ Get Cryptocurrency Price
@cli.command()
@click.argument("symbol")
def price(symbol):
    """Get the current price of a cryptocurrency."""
    price = APIService.get_crypto_price(symbol)
    if price:
        console.print(f"[bold green]{symbol.upper()} Price: ${price}[/bold green]")
    else:
        console.print(f"[bold red]Error: Cryptocurrency '{symbol}' not found.[/bold red]")

# ✅ Convert Cryptocurrency
@cli.command()
@click.argument("symbol")
@click.argument("amount", type=float)
@click.argument("target_currency")
def convert(symbol, amount, target_currency):
    """Convert cryptocurrency to another currency."""
    converted_value = APIService.convert_crypto(symbol, amount, target_currency)
    if converted_value:
        console.print(f"[bold green]{amount} {symbol.upper()} = {converted_value:.2f} {target_currency.upper()}[/bold green]")
    else:
        console.print(f"[bold red]Error: Could not convert {symbol} to {target_currency}[/bold red]")

# ✅ Portfolio Commands
@click.group()
def portfolio():
    """Manage user portfolios."""
    pass

@portfolio.command()
@click.argument("username")
@click.argument("symbol")
@click.argument("quantity", type=float)
def add(username, symbol, quantity):
    """Add cryptocurrency to a user's portfolio."""
    console.print(PortfolioService.add_to_portfolio(username, symbol.upper(), quantity))

@portfolio.command()
@click.argument("username")
def view(username):
    """View a user's portfolio."""
    console.print(PortfolioService.view_user_portfolio(username))

@portfolio.command()
def list():
    """List all user portfolios."""
    console.print(PortfolioService.list_all_portfolios())

cli.add_command(portfolio)

# ✅ Alert Commands
@click.group()
def alert():
    """Set and check price alerts."""
    pass

@alert.command()
@click.argument("symbol")
@click.argument("target_price", type=float)
def set(symbol, target_price):
    """Set a price alert."""
    console.print(AlertService.set_alert(symbol.upper(), target_price))

@alert.command()
def check():
    """Check all active price alerts."""
    console.print(AlertService.check_alerts())

cli.add_command(alert)

# ✅ User Management
@cli.command()
@click.argument("username")
def adduser(username):
    """Add a new user."""
    result = UserService.add_user(username)
    console.print(result)

# ✅ Cryptocurrency Management
@click.group()
def cryptocurrencies():
    """Manage cryptocurrency data."""
    pass

@cryptocurrencies.command()
def list():
    """List all available cryptocurrencies."""
    cryptos = PortfolioService.list_cryptocurrencies()
    if cryptos:
        console.print("[bold green]Available Cryptocurrencies:[/bold green]")
        for crypto in cryptos:
            console.print(f"{crypto.name} ({crypto.symbol}) - ${crypto.price}")
    else:
        console.print("[bold red]No cryptocurrencies found in the database.[/bold red]")

@cryptocurrencies.command()
def update():
    """Update cryptocurrency data from the CoinGecko API."""
    crypto_data = fetch_crypto_data()
    if crypto_data:
        update_cryptocurrencies_table(crypto_data)
        console.print("[bold green]Cryptocurrency data updated successfully![/bold green]")
    else:
        console.print("[bold red]Failed to fetch cryptocurrency data from the API.[/bold red]")

cli.add_command(cryptocurrencies)

# ✅ Main Entry Point
if __name__ == "__main__":
    cli()
