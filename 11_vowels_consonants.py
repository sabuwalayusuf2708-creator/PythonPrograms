def count_vowels_consonants(text):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


if __name__ == "__main__":
    print(count_vowels_consonants("Hello World"))
