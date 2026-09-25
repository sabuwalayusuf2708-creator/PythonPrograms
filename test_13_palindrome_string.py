import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
is_palindrome_string = importlib.import_module("Code.13_palindrome_string").is_palindrome_string

def test_palindrome(): assert is_palindrome_string("madam") is True
def test_not_palindrome(): assert is_palindrome_string("hello") is False
def test_phrase(): assert is_palindrome_string("A man, a plan, a canal: Panama") is True

if __name__ == "__main__":
    for test in [test_palindrome, test_not_palindrome, test_phrase]: test()
    print("All test cases passed.")
