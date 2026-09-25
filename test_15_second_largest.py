import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
second_largest = importlib.import_module("Code.15_second_largest").second_largest

def test_second_largest(): assert second_largest([10, 5, 8, 20, 15]) == 15
def test_duplicates(): assert second_largest([5, 5, 4, 4, 3]) == 4
def test_negative(): assert second_largest([-1, -5, -3]) == -3

if __name__ == "__main__":
    for test in [test_second_largest, test_duplicates, test_negative]: test()
    print("All test cases passed.")
