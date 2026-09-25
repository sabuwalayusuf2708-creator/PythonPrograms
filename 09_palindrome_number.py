def is_palindrome_number(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    print(is_palindrome_number(121))
    print(is_palindrome_number(123))
