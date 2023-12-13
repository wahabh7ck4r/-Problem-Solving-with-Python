# Write a Python function called reverse_elements that takes a list of integers as input and reverses elements within certain segments of the list based on provided start and end indices.

# The function should take the following arguments:

# nums: A list of integers.
# segments: A list of tuples. Each tuple consists of two integers (start, end), indicating the start and end indices (inclusive) of the segment to be reversed.
# Your function should reverse the elements within the specified segments in the list nums and return the modified list.


def reverse_elements(nums, segments):
    for start, end in segments:
        nums[start:end + 1] = nums[start:end + 1][::-1]
    return nums

# Test case
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
segments = [(1, 3), (5, 7)]

result = reverse_elements(nums, segments)
print(result)
