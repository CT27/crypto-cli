import argparse
from rich.console import Console
from services.api_service import APIService 
from services.portfolio_service import PortfolioService

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Crypto CLI Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Price command
    price_parser = subparsers.add_parser("price", help="Get cryptocurrency price")
    price_parser.add_argument("symbol", type=str, help="Cryptocurrency symbol (e.g. bitcoin, ethereum)")

    # Portfolio commands
    portfolio_parser = subparsers.add_parser("portfolio", help="Manage your portfolio")
    portfolio_parser.add_argument("action", choices=["add", "view"], help="Action to perform")
    portfolio_parser.add_argument("symbol", nargs='?', help="Cryptocurrency symbol (e.g. bitcoin)")
    portfolio_parser.add_argument("quantity", type=float, nargs='?', help="Quantity of cryptocurrency")

    args = parser.parse_args()
    if args.command == "price":
        price = APIService.get_crypto_price(args.symbol)
        if price:
            console.print(f"[bold green]{args.symbol.upper()} Price: ${price}[/bold green]")
        else:
            console.print(f"[bold red]Error: Cryptocurrency '{args.symbol}' not found.[/bold red]")
    elif args.command == "portfolio":
        if args.action == "add" and args.symbol and args.quantity:
            console.print(PortfolioService.add_to_portfolio(args.symbol, args.quantity))
        elif args.action == "view":
            console.print(PortfolioService.view_portfolio())
        else:
            console.print("Invalid portfolio command usage.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
