import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
char_frequency = importlib.import_module("Code.14_char_frequency").char_frequency

def test_frequency(): assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
def test_empty(): assert char_frequency("") == {}
def test_spaces_counted(): assert char_frequency("a a") == {"a": 2, " ": 1}

if __name__ == "__main__":
    for test in [test_frequency, test_empty, test_spaces_counted]: test()
    print("All test cases passed.")
