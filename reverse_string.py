# Write a Python function that takes a string as input and returns the reverse of the string without using any built-in reverse functions or slicing.

def reverse_string(string):

    result = ''

    for i in range(len(string)-1,-1,-1):
        result += string[i]

    return result


chcek = reverse_string("this is a book")
print(chcek)