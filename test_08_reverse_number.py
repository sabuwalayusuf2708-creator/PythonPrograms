import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
reverse_number = importlib.import_module("Code.08_reverse_number").reverse_number

def test_reverse(): assert reverse_number(12345) == 54321
def test_trailing_zero(): assert reverse_number(120) == 21
def test_negative(): assert reverse_number(-123) == -321

if __name__ == "__main__":
    for test in [test_reverse, test_trailing_zero, test_negative]: test()
    print("All test cases passed.")
