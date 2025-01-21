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
