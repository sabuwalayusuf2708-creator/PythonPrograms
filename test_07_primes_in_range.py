import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
primes_in_range = importlib.import_module("Code.07_primes_in_range").primes_in_range

def test_range(): assert primes_in_range(10, 20) == [11, 13, 17, 19]
def test_small_range(): assert primes_in_range(1, 3) == [2, 3]
def test_no_primes(): assert primes_in_range(14, 16) == []

if __name__ == "__main__":
    for test in [test_range, test_small_range, test_no_primes]: test()
    print("All test cases passed.")
