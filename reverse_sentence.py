# Write a Python function called reverse_sentence that takes a sentence as a string and reverses the order of words within the sentence. Words are separated by spaces, and the sentence may contain punctuation.


def reverse_sentence(sent):
    words = sent.split()
    rvs_words = words[::-1]
    rvs_sent = " ".join(rvs_words)
    return rvs_sent

sentence = "Thanks! that's helpful"
check = reverse_sentence(sentence)
print(check)