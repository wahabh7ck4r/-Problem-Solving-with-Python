# Write a Python function that takes a string as input and returns a new string where vowels (a, e, i, o, u, and y) are replaced with the character 'o'. All other characters should remain unchanged.


def replace_vowels(string):

    vowels = ['a','e','i','o','u','y']
    result = ''
    for char in string:
        if char in vowels:
            result += 'o'
        else:
            result += char

    return result

user_str = input("Enter a word: ")

check = replace_vowels(user_str)

print(check)

