# Write a Python function that takes a list of integers as input and returns the maximum difference between any two numbers in the list. The function should return 0 if the list contains fewer than two elements.

def Max_diff(nums):
    if len(nums) < 2:
        return 0

    max_num = max(nums)
    min_num = min(nums)

    max_difference = max_num - min_num

    return max_difference 


num_ls = [2,3,5,1,5,6,1,51]

check = Max_diff(num_ls)

print(check)