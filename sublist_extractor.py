# Write a Python function called get_sublist that takes a list and two indices start and end as input, and returns a sublist of the original list from index start (inclusive) to index end (exclusive) using list slicing.

def get_sublist(ls, start, end):
    list_length = len(ls)

    if list_length < end:
        return " list length is smaller then the (end) element you provid " 
    
    new_list = ls[start:end]

    return new_list
    


start = -9
end = -1


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
check = get_sublist(original_list, start, end)
print(check)