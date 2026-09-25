import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
factorial = importlib.import_module("Code.04_factorial").factorial

def test_five(): assert factorial(5) == 120
def test_zero(): assert factorial(0) == 1
def test_one(): assert factorial(1) == 1

if __name__ == "__main__":
    for test in [test_five, test_zero, test_one]: test()
    print("All test cases passed.")
