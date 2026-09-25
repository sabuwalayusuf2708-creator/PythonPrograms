import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
fibonacci_series = importlib.import_module("Code.05_fibonacci_series").fibonacci_series

def test_series(): assert fibonacci_series(6) == [0, 1, 1, 2, 3, 5]
def test_zero_terms(): assert fibonacci_series(0) == []
def test_one_term(): assert fibonacci_series(1) == [0]

if __name__ == "__main__":
    for test in [test_series, test_zero_terms, test_one_term]: test()
    print("All test cases passed.")
