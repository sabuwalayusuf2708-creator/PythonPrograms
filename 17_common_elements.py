def common_elements(list1, list2):
    return list(dict.fromkeys(item for item in list1 if item in list2))


if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
