### **📌 Full List of CLI Commands for Crypto CLI Tool**

Below is a **complete** list of CLI commands you can use, categorized by functionality.

---

## **🚀 1. Cryptocurrency Price & Conversion**

### **🔹 Get the Price of a Cryptocurrency**

```bash
python crypto_cli_tool.py price bitcoin
```

📌 **Example Output**:

```
BITCOIN Price: $34000
```

### **🔹 Convert Cryptocurrency to Another Currency**

```bash
python crypto_cli_tool.py convert bitcoin 1 usd
```

📌 **Example Output**:

```
1 BITCOIN = 34000.00 USD
```

---

## **📂 2. Portfolio Management**

### **🔹 Add a Cryptocurrency to a User’s Portfolio**

```bash
python crypto_cli_tool.py portfolio add candice btc 0.5
```

📌 **Example Output**:

```
Successfully added 0.5 BITCOIN to Candice's portfolio.
```

### **🔹 View a Specific User’s Portfolio**

```bash
python crypto_cli_tool.py portfolio view candice
```

📌 **Example Output**:

```
Portfolio for candice:
Bitcoin (BTC): 0.5 units
Ethereum (ETH): 1.2 units
```

### **🔹 View All Portfolios (All Users)**

```bash
python crypto_cli_tool.py portfolio list
```

📌 **Example Output**:

```
All User Portfolios:

candice's Portfolio:
 - Bitcoin (BTC): 0.5 units
 - Ethereum (ETH): 1.2 units

john's Portfolio:
 - Dogecoin (DOGE): 100.0 units
```

---

## **🔔 3. Price Alerts**

### **🔹 Set a Price Alert for a Cryptocurrency**

```bash
python crypto_cli_tool.py alert set btc 50000
```

📌 **Example Output**:

```
Alert set for BITCOIN at $50000
```

### **🔹 Check All Active Alerts**

```bash
python crypto_cli_tool.py alert check
```

📌 **Example Output**:

```
Active alerts:
BITCOIN: $50000
ETHEREUM: $3500
```

---

## **👤 4. User Management**

### **🔹 Add a New User**

```bash
python crypto_cli_tool.py adduser candice
```

📌 **Example Output**:

```
User 'candice' added successfully.
```

---

## **💰 5. Cryptocurrency Data Management**

### **🔹 List All Available Cryptocurrencies in the Database**

```bash
python crypto_cli_tool.py cryptocurrencies list
```

📌 **Example Output**:

```
Available Cryptocurrencies:
Bitcoin (BTC) - $34000
Ethereum (ETH) - $2400
Dogecoin (DOGE) - $0.07
```

### **🔹 Update Cryptocurrency Data from CoinGecko**

```bash
python crypto_cli_tool.py cryptocurrencies update
```

📌 **Example Output**:

```
Fetching cryptocurrency data from CoinGecko...
Updated: Bitcoin (BTC) - $34000
Updated: Ethereum (ETH) - $2400
Inserted: Solana (SOL) - $120
Cryptocurrency data updated successfully!
```

---

## **🛠 6. Help & Debugging**

### **🔹 View CLI Help Information**

```bash
python crypto_cli_tool.py --help
```

📌 **Example Output**:

```
Crypto CLI Tool

usage: crypto_cli_tool.py [-h] {price,convert,portfolio,alert,adduser,cryptocurrencies} ...

positional arguments:
  price              Get cryptocurrency price
  convert            Convert cryptocurrency to another currency
  portfolio          Manage user portfolio
  alert              Set or check price alerts
  adduser            Add a new user to the database
  cryptocurrencies   Manage cryptocurrency data

optional arguments:
  -h, --help         Show this help message and exit
```

---

## **🎯 Summary of Commands**

| **Category**             | **Command**                                               |
| ------------------------ | --------------------------------------------------------- |
| **Get Crypto Price**     | `python crypto_cli_tool.py price btc`                     |
| **Convert Crypto**       | `python crypto_cli_tool.py convert btc 1 usd`             |
| **Add to Portfolio**     | `python crypto_cli_tool.py portfolio add candice btc 0.5` |
| **View Portfolio**       | `python crypto_cli_tool.py portfolio view candice`        |
| **List All Portfolios**  | `python crypto_cli_tool.py portfolio list`                |
| **Set Alert**            | `python crypto_cli_tool.py alert set bitcoin 50000`       |
| **Check Alerts**         | `python crypto_cli_tool.py alert check`                   |
| **Add User**             | `python crypto_cli_tool.py adduser candice`               |
| **List Cryptos in DB**   | `python crypto_cli_tool.py cryptocurrencies list`         |
| **Update Crypto Prices** | `python crypto_cli_tool.py cryptocurrencies update`       |
| **Help**                 | `python crypto_cli_tool.py --help`                        |

---
