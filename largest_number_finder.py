# Create a Python function that finds the largest number in a given list of integers. The function should take a list of numbers as input and return the largest number present in the list without using any built-in function.


def large_number(nums):
    lrg_num = 0 
    for num in nums:
        if num > lrg_num:
            lrg_num = num
    
    return lrg_num

input_list = [33,22,55,-111,44,-45]
check = large_number(input_list)
print("The largest number in the given list are: " ,check)