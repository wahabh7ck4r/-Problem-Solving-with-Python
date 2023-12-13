# Write a Python function that takes a string as input and returns a dictionary containing the frequency of each word in the string. Consider a word as any sequence of characters separated by spaces.
import string
pun = string.punctuation

def freq_conunter(string):

    words = string.split()

    word_freq = {}

    for word in words:
        word = word.strip(pun)

        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq


sentence = "the sun rises in the east"
check = freq_conunter(sentence)
print(check)