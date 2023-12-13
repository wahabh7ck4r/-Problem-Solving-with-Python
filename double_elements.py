# Write a Python function that takes a list of integers as input and returns a new list where each element is multiplied by 2.

def double_list_elements(nums):
    result = []
    for num in nums:
        mul_num = num * 2
        result.append(mul_num)

    return result

ls = [1, 3, 5, 7]

check = double_list_elements(ls)
print(check)