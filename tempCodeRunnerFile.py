import argparse
import requests
import argcomplete  # Add the import here
from rich.console import Console
from rich.table import Table


API_URL =  "https://api.coingecko.com/api/v3/simple/price"
console = Console()

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

def convert_crypto(symbol, amount, target_currency):
    try:
        response = requests.get(API_URL, params={"ids": symbol.lower(), "vs_currencies": target_currency.lower()})
        data = response.json()
        if symbol.lower() in data:
            rate = data[symbol.lower()][target_currency.lower()]
            converted_amount = amount * rate
            console.print(f"[bold green]{amount} {symbol.upper()} = {converted_amount:.2f} {target_currency.upper()}[/bold green]")
        else:
            console.print(f"[bold red]Error: Cryptocurrency '{symbol}' not found.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error fetching data: {e}[/bold red]")

def main():
    parser = argparse.ArgumentParser(description="Crypto CLI Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Get Price Command
    price_parser = subparsers.add_parser("price", help="Get cryptocurrency price")
    price_parser.add_argument("symbol", type=str, help="Cryptocurrency symbol (e.g. BTC, ETH)")

    # Convert Command
    convert_parser = subparsers.add_parser("convert", help="Convert cryptocurrency to another currency")
    convert_parser.add_argument("symbol", type=str, help="Cryptocurrency symbol (e.g. BTC)")
    convert_parser.add_argument("amount", type=float, help="Amount of cryptocurrency to convert")
    convert_parser.add_argument("target_currency", type=str, help="Target currency (e.g. USD, EUR)")

    # Enable autocomplete for CLI commands
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    if args.command == "price":
        get_crypto_price(args.symbol)
    elif args.command == "convert":
        convert_crypto(args.symbol, args.amount, args.target_currency)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
