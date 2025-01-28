````markdown
# Crypto CLI Tool

`Crypto CLI Tool` is a command-line application that enables users to interact with cryptocurrency data, manage portfolios, set price alerts, and convert currencies. It provides a simple and user-friendly interface for cryptocurrency enthusiasts to fetch real-time data and manage their investments.

---

## Features

- **Get Cryptocurrency Prices**: Retrieve the latest price of a specific cryptocurrency.
- **Currency Conversion**: Convert cryptocurrency amounts to various fiat currencies (e.g., USD, EUR).
- **Manage Portfolios**:
  - Add cryptocurrencies to user portfolios.
  - View detailed portfolios for individual users.
- **Set and Check Price Alerts**:
  - Set alerts for cryptocurrencies when they hit specific prices.
  - Check all active price alerts.
- **User Management**: Add new users to the database for personalized portfolio tracking.

---

## Prerequisites

To use this tool, you need the following:

1. **Python**: Version 3.8 or higher.
2. **Dependencies**: Install required Python packages via `pip`:
   ```bash
   pip install -r requirements.txt
   ```
````

> Ensure `Rich` and `SQLAlchemy` are included in the `requirements.txt`.

3. **Alembic**:

   - Alembic is used for managing database migrations. Ensure the `alembic.ini` file is configured correctly.
   - By default, the database URL in `alembic.ini` is set to:
     ```ini
     sqlalchemy.url = sqlite:///crypto_portfolio.db
     ```
   - Update this URL if you are using a different database.

4. **External API**:

   - The tool fetches cryptocurrency data using the [CoinGecko API](https://www.coingecko.com/).

5. **Database**:
   - A database is used to store user data and portfolio information. Ensure your database models are set up with SQLAlchemy.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/crypto-cli-tool.git
   cd crypto-cli-tool
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   - Configure your database connection in the `models.py` file.
   - Run migrations using Alembic:
     ```bash
     alembic upgrade head
     ```

4. Run the CLI tool:
   ```bash
   python crypto_cli_tool.py
   ```

---

## Usage

The tool supports several commands. Below are examples of each feature:

### 1. Get Cryptocurrency Price

```bash
python crypto_cli_tool.py price bitcoin
```

Output:

```
BITCOIN Price: $34000
```

### 2. Convert Cryptocurrency

```bash
python crypto_cli_tool.py convert bitcoin 1 usd
```

Output:

```
1 BITCOIN = 34000.00 USD
```

### 3. Manage Portfolio

- **Add to Portfolio**:

  ```bash
  python crypto_cli_tool.py portfolio add john bitcoin 0.5
  ```

  Output:

  ```
  Successfully added 0.5 BITCOIN to John's portfolio.
  ```

- **View Portfolio**:
  ```bash
  python crypto_cli_tool.py portfolio view john
  ```
  Output:
  ```
  Portfolio for john:
  Bitcoin (BTC): 0.5 units
  ```

### 4. Set and Check Alerts

- **Set Price Alert**:

  ```bash
  python crypto_cli_tool.py alert set bitcoin 50000
  ```

  Output:

  ```
  Alert set for BITCOIN at $50000
  ```

- **Check Alerts**:
  ```bash
  python crypto_cli_tool.py alert check
  ```
  Output:
  ```
  Active alerts:
  BITCOIN: $50000
  ```

### 5. Add User

```bash
python crypto_cli_tool.py adduser john
```

Output:

```
User 'john' added successfully.
```

---

## Database Migrations with Alembic

This project uses **Alembic** to manage database migrations. Alembic ensures your database schema matches your SQLAlchemy models.

### Setting Up Alembic

1. Ensure Alembic is installed:

   ```bash
   pip install alembic
   ```

2. Configure the `alembic.ini` file:

   - The default database URL is:
     ```ini
     sqlalchemy.url = sqlite:///crypto_portfolio.db
     ```
   - Update this URL if you're using a different database (e.g., PostgreSQL).

3. Apply existing migrations:

   ```bash
   alembic upgrade head
   ```

4. Create a new migration after modifying models:

   ```bash
   alembic revision --autogenerate -m "Description of migration"
   ```

5. Roll back to the previous migration (if needed):
   ```bash
   alembic downgrade -1
   ```

For more details, refer to the [Alembic documentation](https://alembic.sqlalchemy.org/).

---

## Project Structure

```
crypto-cli-tool/
├── crypto_cli_tool.py            # Main CLI tool
├── alembic/
│   ├── env.py                    # Alembic environment configuration
│   ├── versions/                 # Database migration scripts
├── services/
│   ├── alert_service.py          # Handles alerts
│   ├── api_service.py            # Interacts with CoinGecko API
│   ├── portfolio_service.py      # Manages user portfolios
│   ├── user_service.py           # Handles user management
├── Tests/
│   ├── alert_service.py          # Handles alerts
│   ├── api_service.py            # Interacts with CoinGecko API
│   ├── portfolio_service.py      # Manages user portfolios
│   ├── user_service.py           # Handles user management
├── crypto_portfolio.db
├── models.py                      # Database models (User, Portfolio, Cryptocurrency)
├── portfolio.json
├── alerts.json
├── alembic.ini                    # Alembic configuration file
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## Dependencies

The project uses the following Python libraries:

- [Rich](https://rich.readthedocs.io/): For styled console output.
- [Requests](https://docs.python-requests.org/): For API requests.
- [SQLAlchemy](https://www.sqlalchemy.org/): For database interactions.
- [Alembic](https://alembic.sqlalchemy.org/): For managing database migrations.

---

## Future Improvements

- Add support for more cryptocurrency data points (market cap, volume, etc.).
- Implement user authentication for enhanced security.
- Provide historical price charts.
- Add export functionality for portfolio data.
- Integrate email or SMS notifications for price alerts.

---

## Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or create a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- Data provided by [CoinGecko API](https://www.coingecko.com/).
- Inspired by the growing need for accessible cryptocurrency management tools.

```

```
