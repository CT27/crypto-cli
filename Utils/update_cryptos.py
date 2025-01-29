import os
import sqlite3
import requests
import logging

# Configure logging
logging.basicConfig(
    filename="crypto_update.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Database file path (relative to the project directory)
DB_FILE = os.path.join(os.path.dirname(__file__), "../crypto_portfolio.db")

# CoinGecko API URL for fetching market data
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,  # Fetch top 100 cryptocurrencies
    "page": 1
}

def fetch_crypto_data():
    """
    Fetches cryptocurrency data from CoinGecko API.
    Returns:
        list: A list of dictionaries containing cryptocurrency details.
    """
    try:
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status()  # Raise an error if the request fails
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching cryptocurrency data: {e}")
        return []

def update_cryptocurrencies_table(crypto_data):
    """
    Updates the 'cryptocurrencies' table with fetched data from CoinGecko API.

    - If the cryptocurrency exists, it updates the price.
    - If the cryptocurrency doesn't exist, it inserts it as a new entry.

    Args:
        crypto_data (list): A list of cryptocurrency data from the API.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Ensure the cryptocurrencies table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cryptocurrencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            symbol VARCHAR NOT NULL UNIQUE,
            price FLOAT NOT NULL
        )
    """)

    for crypto in crypto_data:
        name = crypto["name"]
        symbol = crypto["symbol"].upper()  # Store symbols in uppercase
        price = crypto["current_price"]

        # Check if the cryptocurrency already exists
        cursor.execute("SELECT id FROM cryptocurrencies WHERE symbol = ?", (symbol,))
        result = cursor.fetchone()

        if result:
            # Update the price if it exists
            cursor.execute(
                "UPDATE cryptocurrencies SET price = ? WHERE symbol = ?",
                (price, symbol),
            )
            logging.info(f"Updated: {name} ({symbol}) - ${price}")
        else:
            # Insert new cryptocurrency
            cursor.execute(
                "INSERT INTO cryptocurrencies (name, symbol, price) VALUES (?, ?, ?)",
                (name, symbol, price),
            )
            logging.info(f"Inserted: {name} ({symbol}) - ${price}")

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("✅ Cryptocurrency database updated successfully!")

def main():
    """
    Main function to fetch and update cryptocurrency data.
    """
    print("🔄 Fetching cryptocurrency data from CoinGecko...")
    crypto_data = fetch_crypto_data()
    
    if crypto_data:
        update_cryptocurrencies_table(crypto_data)
    else:
        print("❌ Failed to fetch cryptocurrency data.")

if __name__ == "__main__":
    main()
