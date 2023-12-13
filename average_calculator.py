# Write a Python function called calculate_average that takes in a list of numbers as an argument and returns the average (mean) of those numbers.

def calculate_average(nums):
    if len(nums) <= 0 :
        return 0

    total = sum(nums)
    avg = total / len(nums)

    return avg

ls = [1, 2, 3, 4, 5]
check = calculate_average(ls)
print("The avrage of ", ls ," are ", check)
    