import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
common_elements = importlib.import_module("Code.17_common_elements").common_elements

def test_common(): assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
def test_no_common(): assert common_elements([1, 2], [3, 4]) == []
def test_duplicates_preserve_first_order(): assert common_elements([1, 2, 2, 3], [2, 3]) == [2, 3]

if __name__ == "__main__":
    for test in [test_common, test_no_common, test_duplicates_preserve_first_order]: test()
    print("All test cases passed.")
