# Write a Python function that takes a list of strings as input and returns a new list containing only the strings that have a length greater than a specified length. The function should accept two arguments: the list of strings and the minimum length. It should return a new list containing only the strings from the original list that have a length greater than the specified minimum length.



# Function to filter strings by length
def string_filter(strings, min_len):
    result = [] 

    for string in strings:
        if len(string) > min_len:  #  '>' for strings greater than specified length
            result.append(string)

    return result 

input_list = ["apple", "banana", "kiwi", "orange", "grape", "watermelon"]
min_len = 5 

filtered_strings = string_filter(input_list, min_len)
print(f"Strings with length greater than {min_len}: {filtered_strings}")
