# Write a Python function called chunk_list that takes a list and chunk size as input and returns a new list with the original list split into chunks of the specified size using list slicing.

def chunk_list(lst, chunk_size):
    chunk_lst = []

    for i in range(0, len(lst), chunk_size):
        chunk_lst.append(lst[i:i+chunk_size])

    return chunk_lst

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
check = chunk_list(original_list, 8)
print(check)

