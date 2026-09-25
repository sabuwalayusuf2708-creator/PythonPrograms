import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
remove_duplicates = importlib.import_module("Code.16_remove_duplicates").remove_duplicates

def test_duplicates(): assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
def test_no_duplicates(): assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
def test_empty(): assert remove_duplicates([]) == []

if __name__ == "__main__":
    for test in [test_duplicates, test_no_duplicates, test_empty]: test()
    print("All test cases passed.")
