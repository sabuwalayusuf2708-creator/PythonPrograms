import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
missing_number = importlib.import_module("Code.18_missing_number").missing_number

def test_missing_middle(): assert missing_number([1, 2, 3, 5]) == 4
def test_missing_one(): assert missing_number([2, 3, 4, 5]) == 1
def test_missing_last(): assert missing_number([1, 2, 3, 4]) == 5

if __name__ == "__main__":
    for test in [test_missing_middle, test_missing_one, test_missing_last]: test()
    print("All test cases passed.")
