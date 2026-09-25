def char_frequency(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


if __name__ == "__main__":
    print(char_frequency("hello"))
