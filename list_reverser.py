# Write a Python function called reverse_list that takes a list as input and returns a new list containing the elements of the original list in reverse order using list slicing.

def reverse_list(lst):
    rsv_lst = lst[::-1]
    return rsv_lst


original_list = [1, 2, 3, 4, 5]
check = reverse_list(original_list)
print(check)
