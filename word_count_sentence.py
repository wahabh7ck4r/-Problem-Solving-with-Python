# Write a Python program that takes a sentence as input from the user and counts the number of words in that sentence. Consider words to be separated by spaces.

def Word_counter(sentence):
    word = sentence.split()

    total_word = len(word)

    return total_word



chcek = Word_counter("This is a sentence for testing    purpose")
print("The total word in the given sentence are: ", chcek)
