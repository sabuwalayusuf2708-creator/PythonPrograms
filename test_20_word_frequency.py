import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
word_frequency = importlib.import_module("Code.20_word_frequency").word_frequency

def test_frequency(): assert word_frequency("Python is easy and Python is powerful") == {"python": 2, "is": 2, "easy": 1, "and": 1, "powerful": 1}
def test_empty(): assert word_frequency("") == {}
def test_case_insensitive(): assert word_frequency("Hello hello HELLO") == {"hello": 3}

if __name__ == "__main__":
    for test in [test_frequency, test_empty, test_case_insensitive]: test()
    print("All test cases passed.")
