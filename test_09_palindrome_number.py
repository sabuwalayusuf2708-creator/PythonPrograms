import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
is_palindrome_number = importlib.import_module("Code.09_palindrome_number").is_palindrome_number

def test_palindrome(): assert is_palindrome_number(121) is True
def test_not_palindrome(): assert is_palindrome_number(123) is False
def test_single_digit(): assert is_palindrome_number(7) is True

if __name__ == "__main__":
    for test in [test_palindrome, test_not_palindrome, test_single_digit]: test()
    print("All test cases passed.")
