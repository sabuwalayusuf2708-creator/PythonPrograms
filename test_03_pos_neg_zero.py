import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
check_number = importlib.import_module("Code.03_pos_neg_zero").check_number

def test_positive(): assert check_number(5) == "Positive"
def test_negative(): assert check_number(-5) == "Negative"
def test_zero(): assert check_number(0) == "Zero"

if __name__ == "__main__":
    for test in [test_positive, test_negative, test_zero]: test()
    print("All test cases passed.")
