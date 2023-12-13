# Write a Python function that takes a list of strings as input and returns a new list containing the lengths of those strings that have a length greater than 3.

def string_len_grater_than_3(ls):
    ls_len = []

    for str in ls:
        if len(str) > 3:
            len_str = len(str)
            ls_len.append(len_str)

    return ls_len

input_ls = ['apple', 'banana', 'kiwi', 'orange', 'strawberry']

check = string_len_grater_then_3(input_ls)
print(check)