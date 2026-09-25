def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two distinct numbers")
    return unique_numbers[1]


if __name__ == "__main__":
    print(second_largest([10, 5, 8, 20, 15]))
