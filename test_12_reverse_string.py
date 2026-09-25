import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
reverse_string = importlib.import_module("Code.12_reverse_string").reverse_string

def test_reverse(): assert reverse_string("Python") == "nohtyP"
def test_empty(): assert reverse_string("") == ""
def test_spaces(): assert reverse_string("hello world") == "dlrow olleh"

if __name__ == "__main__":
    for test in [test_reverse, test_empty, test_spaces]: test()
    print("All test cases passed.")
