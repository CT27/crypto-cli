import argparse
from rich.console import Console
from services.alert_service import AlertService
from services.api_service import APIService
from services.portfolio_service import PortfolioService
from services.user_service import UserService
from Utils.update_cryptos import fetch_crypto_data, update_cryptocurrencies_table  # Import update functions

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Crypto CLI Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Price command
    price_parser = subparsers.add_parser("price", help="Get cryptocurrency price")
    price_parser.add_argument("symbol", type=str, help="Cryptocurrency symbol (e.g., bitcoin, ethereum)")

    # Convert commands
    convert_parser = subparsers.add_parser("convert", help="Convert cryptocurrency to another currency")
    convert_parser.add_argument("symbol", type=str, help="Cryptocurrency symbol (e.g., bitcoin)")
    convert_parser.add_argument("amount", type=float, help="Amount of cryptocurrency to convert")
    convert_parser.add_argument("target_currency", type=str, help="Target currency (e.g., USD, EUR)")

    # Portfolio commands
    portfolio_parser = subparsers.add_parser("portfolio", help="Manage user portfolio")
    portfolio_parser.add_argument("action", choices=["add", "view"], help="Action to perform")
    portfolio_parser.add_argument("username", type=str, help="Username of the user")
    portfolio_parser.add_argument("symbol", nargs='?', help="Cryptocurrency symbol (e.g., bitcoin)")
    portfolio_parser.add_argument("quantity", type=float, nargs='?', help="Quantity of cryptocurrency")

    # Alert commands
    alert_parser = subparsers.add_parser("alert", help="Set or check price alerts")
    alert_parser.add_argument("action", choices=["set", "check"], help="Action to perform")
    alert_parser.add_argument("symbol", nargs='?', help="Cryptocurrency symbol (e.g., bitcoin)")
    alert_parser.add_argument("target_price", type=float, nargs='?', help="Target price for alert")

    # Add user command
    user_parser = subparsers.add_parser("adduser", help="Add a new user to the database")
    user_parser.add_argument("username", type=str, help="Username to add")

    # Cryptocurrency management commands
    crypto_parser = subparsers.add_parser("cryptocurrencies", help="Manage cryptocurrency data")
    crypto_subparsers = crypto_parser.add_subparsers(dest="crypto_action")

    # List all cryptocurrencies
    crypto_list_parser = crypto_subparsers.add_parser("list", help="List all available cryptocurrencies")

    # Update cryptocurrency data
    crypto_update_parser = crypto_subparsers.add_parser("update", help="Update cryptocurrency data from the CoinGecko API")

    args = parser.parse_args()

    if args.command == "price":
        price = APIService.get_crypto_price(args.symbol)
        if price:
            console.print(f"[bold green]{args.symbol.upper()} Price: ${price}[/bold green]")
        else:
            console.print(f"[bold red]Error: Cryptocurrency '{args.symbol}' not found.[/bold red]")

    elif args.command == "convert":
        converted_value = APIService.convert_crypto(args.symbol, args.amount, args.target_currency)
        if converted_value:
            console.print(f"[bold green]{args.amount} {args.symbol.upper()} = {converted_value:.2f} {args.target_currency.upper()}[/bold green]")
        else:
            console.print(f"[bold red]Error: Could not convert {args.symbol} to {args.target_currency}[/bold red]")

    elif args.command == "portfolio":
        if args.action == "add" and args.username and args.symbol and args.quantity:
            console.print(PortfolioService.add_to_portfolio(args.username, args.symbol.upper(), args.quantity))
        elif args.action == "view" and args.username:
            console.print(PortfolioService.view_user_portfolio(args.username))
        else:
            console.print("[bold red]Invalid portfolio command usage.[/bold red]")

    elif args.command == "alert":
        if args.action == "set" and args.symbol and args.target_price:
            console.print(AlertService.set_alert(args.symbol.upper(), args.target_price))
        elif args.action == "check":
            console.print(AlertService.check_alerts())
        else:
            console.print("[bold red]Invalid alert command usage.[/bold red]")

    elif args.command == "adduser":
        result = UserService.add_user(args.username)
        console.print(result)

    elif args.command == "cryptocurrencies":
        if args.crypto_action == "list":
            cryptos = PortfolioService.list_cryptocurrencies()
            if cryptos:
                console.print("[bold green]Available Cryptocurrencies:[/bold green]")
                for crypto in cryptos:
                    console.print(f"{crypto.name} ({crypto.symbol}) - ${crypto.price}")
            else:
                console.print("[bold red]No cryptocurrencies found in the database.[/bold red]")

        elif args.crypto_action == "update":
            crypto_data = fetch_crypto_data()
            if crypto_data:
                update_cryptocurrencies_table(crypto_data)
                console.print("[bold green]Cryptocurrency data updated successfully![/bold green]")
            else:
                console.print("[bold red]Failed to fetch cryptocurrency data from the API.[/bold red]")

        else:
            console.print("[bold red]Invalid cryptocurrency command usage.[/bold red]")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
