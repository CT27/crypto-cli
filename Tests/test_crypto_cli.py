import subprocess

def test_price_command():
    result = subprocess.run(['python', 'crypto_cli_tool.py', 'price', 'BTC'], capture_output=True, text=True)
    assert 'BTC Price' in result.stdout

def test_convert_command():
    result = subprocess.run(['python', 'crypto_cli_tool.py', 'convert', 'BTC', '0.1', 'USD'], capture_output=True, text=True)
    assert 'BTC' in result.stdout
