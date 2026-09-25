import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
find_duplicates = importlib.import_module("Code.19_find_duplicates").find_duplicates

def test_duplicates(): assert find_duplicates([1, 2, 2, 3, 4, 4, 5]) == [2, 4]
def test_no_duplicates(): assert find_duplicates([1, 2, 3]) == []
def test_multiple_occurrences(): assert find_duplicates([1, 1, 1, 2, 2]) == [1, 2]

if __name__ == "__main__":
    for test in [test_duplicates, test_no_duplicates, test_multiple_occurrences]: test()
    print("All test cases passed.")
