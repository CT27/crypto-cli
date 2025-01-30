from subprocess import run

def test_price_command():
    result = run(['python', 'cli.py', 'price', 'bitcoin'], capture_output=True, text=True)
    assert 'BITCOIN Price' in result.stdout
