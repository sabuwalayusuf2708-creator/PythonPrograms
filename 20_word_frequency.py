import re


def word_frequency(sentence):
    words = re.findall(r"[A-Za-z0-9]+", sentence.lower())
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


if __name__ == "__main__":
    print(word_frequency("Python is easy and Python is powerful"))
