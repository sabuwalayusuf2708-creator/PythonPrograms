import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
sum_of_digits = importlib.import_module("Code.10_sum_of_digits").sum_of_digits

def test_sum(): assert sum_of_digits(12345) == 15
def test_zero(): assert sum_of_digits(0) == 0
def test_negative(): assert sum_of_digits(-123) == 6

if __name__ == "__main__":
    for test in [test_sum, test_zero, test_negative]: test()
    print("All test cases passed.")
