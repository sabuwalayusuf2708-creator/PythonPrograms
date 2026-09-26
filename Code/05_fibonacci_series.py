def fibonacci_series(n):
    if n < 0:
        raise ValueError("Number of terms cannot be negative")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    print(fibonacci_series(8))
