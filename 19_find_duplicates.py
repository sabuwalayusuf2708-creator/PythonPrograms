def find_duplicates(items):
    seen = set()
    duplicates = []
    duplicate_set = set()
    for item in items:
        if item in seen and item not in duplicate_set:
            duplicates.append(item)
            duplicate_set.add(item)
        seen.add(item)
    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 2, 3, 4, 4, 5]))
