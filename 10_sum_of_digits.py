def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


if __name__ == "__main__":
    print(sum_of_digits(12345))
