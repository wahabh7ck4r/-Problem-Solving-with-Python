# Write a Python function that takes a string as input and returns the most common character in the string. If there are multiple characters with the same highest frequency, return all of them in alphabetical order.


def Max_Common_Char(string):
    letters = list(string)
    com_word_ratio = {}

    # Count the frequency of each character
    for letter in letters:
        if letter in com_word_ratio:
            com_word_ratio[letter] += 1
        else:
            com_word_ratio[letter] = 1

    # Find the maximum frequency
    max_freq = max(com_word_ratio.values()) if com_word_ratio else 0

    # Filter characters with the maximum frequency
    most_common = [char for char, freq in com_word_ratio.items() if freq == max_freq]

    # Sort the most common characters alphabetically
    most_common_sorted = sorted(most_common)

    return most_common_sorted

# Test the function
input_string = "hello there"
result = Max_Common_Char(input_string)
print(result)


