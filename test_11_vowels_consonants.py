import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import importlib
count_vowels_consonants = importlib.import_module("Code.11_vowels_consonants").count_vowels_consonants

def test_counts(): assert count_vowels_consonants("Hello") == (2, 3)
def test_only_vowels(): assert count_vowels_consonants("AEIOU") == (5, 0)
def test_only_consonants(): assert count_vowels_consonants("xyz") == (0, 3)

if __name__ == "__main__":
    for test in [test_counts, test_only_vowels, test_only_consonants]: test()
    print("All test cases passed.")
