# Write a Python function called count_words_starting_with_letter that takes a string sentence and a letter start_letter as input. The function should count the number of words in the sentence that start with the specified start_letter (case-insensitive).

def count_words_starting_with_letter(sentence, start_letter):
    specific_word = 0
    sentence = sentence.lower()
    start_letter = start_letter.lower()

    words = sentence.split()

    for word in words:
        if word.startswith(start_letter):
            specific_word += 1

    return f"The total specific word in the sentence: {specific_word}"

start_letter = 't'
input_string = "The quick brown fox jump over the lazy dog"
 
check = count_words_starting_with_letter(input_string,start_letter)
print(check)
