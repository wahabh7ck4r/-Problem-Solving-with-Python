# Write a Python function that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'A' (case-insensitive) and have a length of 3 or more characters. If there are no qualifying strings, the function should return an empty list.


def filter_starting_with_A():
    total_words = int(input("How many words do you want to enter in a list? "))
    user_list = [input(f"Enter word {i + 1}: ") for i in range(total_words)]

    filter_list = []

    for word in user_list:
        # Check if word starts with 'A' (case-insensitive) and has length ≥ 3
        if word.lower().startswith("a") and len(word) >= 3:
            filter_list.append(word)
        
    return filter_list

filtered_words = filter_starting_with_A()
print(filtered_words)
