def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result


if __name__ == "__main__":
    print(reverse_string("Python"))
