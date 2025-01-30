import subprocess

def test_price_command():
    result = subprocess.run(['python', 'cli.py', 'price', 'bitcoin'], capture_output=True, text=True)
    assert 'BITCOIN Price' in result.stdout

def test_convert_command():
    result = subprocess.run(['python', 'cli.py', 'convert', 'bitcoin', '0.1', 'USD'], capture_output=True, text=True)
    assert 'bitcoin'.upper() in result.stdout.upper()

