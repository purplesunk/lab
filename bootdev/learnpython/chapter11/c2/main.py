def count_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    unique_vowels = set()
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count = vowel_count + 1
            unique_vowels.add(char)

    return vowel_count, unique_vowels
