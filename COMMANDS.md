## **🎯 Summary of Commands**

| **Category**             | **Command**                                         |
| ------------------------ | --------------------------------------------------- |
| **Get Crypto Price**     | `python cli.py price bitcoin` ✅                    |
| **Convert Crypto**       | `python cli.py convert bitcoin 1 usd` ✅            |
| **Add to Portfolio**     | `python cli.py portfolio add candice bitcoin 0.5`✅ |
| **View Portfolio**       | `python cli.py portfolio view candice` ✅           |
| **List All Portfolios**  | `python cli.py portfolio list` ✅                   |
| **Set Alert**            | `python cli.py alert set bitcoin 100000`✅          |
| **Check Alerts**         | `python cli.py alert check` ✅                      |
| **Add User**             | `python cli.py adduser candice` ✅                  |
| **List Cryptos in DB**   | `python cli.py cryptocurrencies list`✅             |
| **Update Crypto Prices** | `python cli.py cryptocurrencies update` ✅          |
| **Help**                 | `python cli.py --help` ✅                           |

---

#Testing commands
TESTING=1 pytest

#SQL Commands
sqlite3 crypto_portfolio.db

1. List All Users
   SELECT \* FROM users;

2. List All Cryptocurrencies
   SELECT \* FROM cryptocurrencies;

3. View All Portfolios with User and Cryptocurrency Details
   SELECT u.username, c.name AS crypto_name, c.symbol, p.quantity
   FROM portfolios p
   JOIN users u ON p.user_id = u.id
   JOIN cryptocurrencies c ON p.crypto_id = c.id;

4. View a Specific User's Portfolio
   SELECT u.username, c.name AS crypto_name, c.symbol, p.quantity
   FROM portfolios p
   JOIN users u ON p.user_id = u.id
   JOIN cryptocurrencies c ON p.crypto_id = c.id
   WHERE u.username = 'candice';

#Alembic :
run to create a script for review:
alembic revision --autogenerate -m "insert message"

apply the migration:
alembic upgrade head

rollback:
alembic downgrade -1
or:
alembic downgrade {previous_revision_id}

view the last applied migration:
alembic current

view the history of all migrations
alembic history
