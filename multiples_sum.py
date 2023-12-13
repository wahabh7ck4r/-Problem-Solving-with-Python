# Write a Python function that takes a list of integers as input and returns the sum of the elements in the list that are multiples of 3 or 5.


def sum_of_multiples_of_3_or_5(num_list):

    multiples_num = []

    for num in num_list:
        if num % 3 == 0 or num % 5 == 0:
            multiples_num.append(num)

    total_sum = sum(multiples_num)

    return total_sum


ls = [3,2,2,2,2,2,16,17]

check = sum_of_multiples_of_3_or_5(ls)

print(check)