def remove_duplicates(items):
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
