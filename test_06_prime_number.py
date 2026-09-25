import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
is_prime = importlib.import_module("Code.06_prime_number").is_prime

def test_prime(): assert is_prime(17) is True
def test_not_prime(): assert is_prime(18) is False
def test_small_numbers(): assert is_prime(1) is False

if __name__ == "__main__":
    for test in [test_prime, test_not_prime, test_small_numbers]: test()
    print("All test cases passed.")
