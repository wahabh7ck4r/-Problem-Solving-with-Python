# Write a Python function that checks whether a given string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

def palindrome_checker():
    word = input("Enter a word or phrase to check if it's a palindrome: ")
    # Convert the input to lowercase and remove spaces/punctuation
    processed_word = ''.join(char.lower() for char in word if char.isalnum())

    # Compare the processed word with its reverse to check for a palindrome
    if processed_word == processed_word[::-1]:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome.")


palindrome_checker()

