README.md

# ---------

# # Crypto CLI Tool

# A simple command-line tool to fetch cryptocurrency prices and perform conversions.

#

# ## Installation

# ```

# pip install -r requirements.txt

# ```

#

# ## Usage

# ```

# python crypto_cli_tool.py price bitcoin

# python crypto_cli_tool.py convert bitcoin 0.1 USD

# python crypto_cli_tool.py price ethereum

# python crypto_cli_tool.py convert ethereum 2 eur

# ```

# Help and Usage Guidance

# python crypto_cli_tool.py --help

#

# ## License

# MIT License

#Check Cryptocurrency Prices:
#python crypto_cli_tool.py price bitcoin

#commands:

# price Get cryptocurrency price

    $ python crypto_cli_tool.py price bitcoin
    $ python crypto_cli_tool.py price bitcoin

# portfolio Manage your portfolio

    $ python crypto_cli_tool.py portfolio add bitcoin 1.0 # TO ADD
    $ python crypto_cli_tool.py portfolio view #TO VIEW
    $ rm portfolio.json #RESET OR CLEAR PORTFOLIO

# alert Set or check price alerts

    $ python crypto_cli_tool.py alert check #CHECK ALL ALERTS
    $ cat alerts.json #VIEW ALL ALERTS
    $ nano alerts.json #OPENS A TEXT EDITOR
    $ python crypto_cli_tool.py alert set ethereum 3000 #SET AN ALERT
    $ echo "{}" > alerts.json # CLEARS THE ENTIRE LIST

# convert Convert cryptocurrency to another currency

    $ python crypto_cli_tool.py convert ethereum 5 jpy
    $ python crypto_cli_tool.py convert bitcoin 1 gbp

Based on the provided project structure, services, models, and CLI tool, your application is a **Cryptocurrency Portfolio Management CLI Tool** with the following core functionalities:

### 1. **Cryptocurrency Price Retrieval**

- **Command:** `price <symbol>`
- **Functionality:**
  - Fetches the latest price of a given cryptocurrency (e.g., Bitcoin, Ethereum) in USD.
  - Uses the `APIService` to call the CoinGecko API and retrieve real-time cryptocurrency prices.

### 2. **Cryptocurrency Conversion**

- **Command:** `convert <symbol> <amount> <target_currency>`
- **Functionality:**
  - Converts a given amount of cryptocurrency (e.g., Bitcoin) into another currency (e.g., USD, EUR).
  - Fetches the conversion rate from the CoinGecko API using `APIService`.

### 3. **Portfolio Management**

- **Command:** `portfolio add <symbol> <quantity>`
- **Functionality:**
  - Adds a specified quantity of cryptocurrency to the user's portfolio.
  - Stores portfolio data in a JSON file (`portfolio.json`) using the `PortfolioService`.
- **Command:** `portfolio view`
- **Functionality:**
  - Displays the user's cryptocurrency portfolio, showing current holdings.
  - Reads the stored portfolio data from the JSON file.

### 4. **Price Alerts Management**

- **Command:** `alert set <symbol> <target_price>`
- **Functionality:**
  - Sets a price alert for a specified cryptocurrency at a given target price.
  - Saves alerts to a JSON file (`alerts.json`) via the `AlertService`.
- **Command:** `alert check`
- **Functionality:**
  - Checks and displays any existing price alerts.
  - Retrieves stored alerts from the JSON file.

### 5. **Database Integration (SQLAlchemy Models)**

- The project uses an SQLite database (`crypto_portfolio.db`) to store:
  - **Users:** Tracks different users who own portfolios.
  - **Cryptocurrencies:** Stores available cryptocurrencies with their name and symbol.
  - **Portfolios:** Links users with cryptocurrencies and stores the quantity owned.
- SQLAlchemy ORM is used to interact with the database, providing persistence for user portfolios.

### 6. **Command-Line Interface (CLI)**

- The tool provides a user-friendly interface via `argparse` and uses the `rich` library for colorful output.
- Commands allow users to interact with the tool efficiently without needing a graphical interface.

### 7. **Project Structure Overview**

- **Main files and directories:**
  - `crypto_cli_tool.py`: The main CLI application.
  - `services/`: Contains core logic for alerts, API calls, and portfolio management.
  - `models.py`: Defines database schema using SQLAlchemy.
  - `Pipfile & Pipfile.lock`: Dependency management for the project using Pipenv.
  - `Tests/`: Directory likely containing unit tests to validate application functionality.

---

### **In Summary, This Application:**

- Allows users to **track and manage** their cryptocurrency portfolio via the command line.
- Provides **real-time price updates** and conversions using the CoinGecko API.
- Enables users to **set and check alerts** for their favorite cryptocurrencies.
- Stores portfolio data in both JSON files and an SQLite database for persistence.
- Offers a command-line interface for easy usage without requiring a web or desktop application.

---

Would you like guidance on extending or optimizing this application?
