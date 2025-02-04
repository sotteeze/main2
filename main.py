def process_string(input_string):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    vowel_letters = sorted([char for char in input_string if char in vowels])
    consonant_letters = sorted([char for char in input_string if char in consonants])

    vowels_str = ''.join(vowel_letters)

    has_few_consonants = len(consonant_letters) < 4

    consonants_str = ''.join(consonant_letters)

    return (vowels_str, has_few_consonants, consonants_str)

input_string = "abcdefg"
result = process_string(input_string)
print(result)