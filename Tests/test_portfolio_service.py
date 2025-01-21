import unittest
import os
import json
from services.portfolio_service import PortfolioService

class TestPortfolioService(unittest.TestCase):

    def setUp(self):
        # Create a temporary portfolio file for testing
        self.test_portfolio_file = "test_portfolio.json"
        PortfolioService.PORTFOLIO_FILE = self.test_portfolio_file

    def tearDown(self):
        # Cleanup test file after tests
        if os.path.exists(self.test_portfolio_file):
            os.remove(self.test_portfolio_file)

    def test_add_to_portfolio(self):
        result = PortfolioService.add_to_portfolio("bitcoin", 1.5)
        self.assertEqual(result, "Added 1.5 BITCOIN to portfolio.")
        with open(self.test_portfolio_file, "r") as f:
            data = json.load(f)
        self.assertEqual(data["bitcoin"], 1.5)

    def test_view_empty_portfolio(self):
        result = PortfolioService.view_portfolio()
        self.assertEqual(result, "Your portfolio is empty.")

    def test_view_portfolio(self):
        PortfolioService.add_to_portfolio("ethereum", 3.0)
        portfolio = PortfolioService.view_portfolio()
        self.assertIn("ethereum", portfolio)
        self.assertEqual(portfolio["ethereum"], 3.0)

    def test_load_portfolio_file_not_exist(self):
        os.remove(self.test_portfolio_file) if os.path.exists(self.test_portfolio_file) else None
        portfolio = PortfolioService.load_portfolio()
        self.assertEqual(portfolio, {})

if __name__ == "__main__":
    unittest.main()

