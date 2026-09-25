import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
even_odd = importlib.import_module("Code.01_even_odd").even_odd

def test_even(): assert even_odd(10) == "Even"
def test_odd(): assert even_odd(7) == "Odd"
def test_zero(): assert even_odd(0) == "Even"
def test_negative_even(): assert even_odd(-4) == "Even"
def test_negative_odd(): assert even_odd(-5) == "Odd"

if __name__ == "__main__":
    for test in [test_even, test_odd, test_zero, test_negative_even, test_negative_odd]: test()
    print("All test cases passed.")
