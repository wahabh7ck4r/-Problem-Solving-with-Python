# write a program to convert a number in words(like:- 1 to one)

import inflect

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

# Taking user input
num = int(input("Enter a number: "))

# Convert number to words
result = number_to_words(num)
print(f"The number {num} in words is: {result}")

    