def missing_number(numbers):
    n = len(numbers) + 1
    expected = n * (n + 1) // 2
    return expected - sum(numbers)


if __name__ == "__main__":
    print(missing_number([1, 2, 3, 5]))
