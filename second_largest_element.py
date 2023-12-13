# Write a Python function that takes a list of integers as input and returns the second largest element from the list. If there are multiple occurrences of the second largest element, return any one of them

def second_largest_number(nums):
    unique_num = sorted(set(nums), reverse=True)
    
    if len(unique_num) < 2:
        print("list has less then two unique numbers")
        return False
    second_larg_num = unique_num[1]

    return second_larg_num


numbers = [3,3,3,3,35]
chceck = second_largest_number(numbers)

if chceck:
    print("The Second largest number is {}".format(chceck))
else:
    print("\n The second largest number is not found due less ratio of unique number")
