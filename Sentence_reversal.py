# Write a function that takes in a string containing a sentence and returns a new string with the words reversed, maintaining the order of words but reversing the order of the words themselves.


def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

user_input = input("Enter a sentence: ")
result = reverse_sentence(user_input)
print("Reversed sentence:", result)


