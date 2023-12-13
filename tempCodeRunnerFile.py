# Write a Python function called get_even_numbers that takes a list of integers as input and returns a new list containing only the numbers from the original list that is on even index, using list slicing.

def even_Index(nums):
    even_num = nums[::2]
    return even_num


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = get_even_numbers(input_list)
print(check)