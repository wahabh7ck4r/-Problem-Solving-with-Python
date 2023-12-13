# Write a Python function that takes a string as input and returns a new string where each character in the original string is doubled. For example, if the input string is "hello", the output should be "hheelllloo"

def double_characters_by_index(string):
    result = ''
    for i, char in enumerate(string):
        result += char * 2  # Duplicate each character 
    return result

# Test the function
input_string = "python"
output_string = double_characters_by_index(input_string)
print(output_string)



