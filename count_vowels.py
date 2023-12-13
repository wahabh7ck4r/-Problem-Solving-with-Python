# Write a Python function that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string. The function should be case-insensitive, meaning it should count both uppercase and lowercase vowels.


def Vowel_counter(string):
    total_vowel = 0
    vol = ['a','e','i','o','u']

    string = string.lower()

    for char in string:
        if char in vol:
            total_vowel = total_vowel + 1

    return f"The total vowels in the given string are: {total_vowel}"


check = Vowel_counter("python is the best programin language.")
print(check)
