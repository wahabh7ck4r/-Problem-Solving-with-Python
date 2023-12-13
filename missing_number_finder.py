# Write a Python function called find_missing_number that takes in a list of integers from 1 to n (inclusive) with one number missing. The list is unsorted, and it's guaranteed that only one number is missing from the sequence.


def find_missing_number(nums):
    result = 0
    max_num = max(nums)

    for num in range(max_num+1):
        if num not in nums:
            result = num
    
    return f"The missing number in the list is: {result}"

input_list = [3, 7, 1, 2, 8, 6, 5]
check = find_missing_number(input_list)
print(check)
    
