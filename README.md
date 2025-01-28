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

3. **External API**:

   - The tool fetches cryptocurrency data using the [CoinGecko API](https://www.coingecko.com/).

4. **Database**:
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
   - Run migrations or create necessary tables as per your schema.

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

## Project Structure

```
crypto-cli-tool/
├── crypto_cli_tool.py          # Main CLI tool
├── services/
│   ├── alert_service.py        # Handles alerts
│   ├── api_service.py          # Interacts with CoinGecko API
│   ├── portfolio_service.py    # Manages user portfolios
│   ├── user_service.py         # Handles user management
├── models.py                   # Database models (User, Portfolio, Cryptocurrency)
├── alerts.json                 # JSON file for storing alerts
├── portfolio.json              # (Optional) Legacy portfolio storage
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Dependencies

The project uses the following Python libraries:

- [Rich](https://rich.readthedocs.io/): For styled console output.
- [Requests](https://docs.python-requests.org/): For API requests.
- [SQLAlchemy](https://www.sqlalchemy.org/): For database interactions.

---

## Configuration

- **API Base URL**: Set to the CoinGecko API for price and conversion data.
- **Alerts and Portfolio Storage**:
  - Alerts are stored in `alerts.json`.
  - Portfolio data is stored in the database and optionally in `portfolio.json`.

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

Feel free to adjust the project URL, future improvements, or additional credits as per your specific needs.
```
