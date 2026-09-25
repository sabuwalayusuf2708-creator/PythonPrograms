def is_palindrome_string(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome_string("madam"))
    print(is_palindrome_string("hello"))
