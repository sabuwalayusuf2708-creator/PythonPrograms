import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
largest_of_three = importlib.import_module("Code.02_largest_of_three").largest_of_three

def test_largest(): assert largest_of_three(10, 25, 15) == 25
def test_negative(): assert largest_of_three(-1, -5, -3) == -1
def test_equal(): assert largest_of_three(7, 7, 7) == 7

if __name__ == "__main__":
    for test in [test_largest, test_negative, test_equal]: test()
    print("All test cases passed.")
