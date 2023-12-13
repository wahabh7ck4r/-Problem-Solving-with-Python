# Create a Python function that takes a list of numbers as input and returns a new list with only the elements that are divisible by a specific divisor. The function should take two arguments: the list of numbers and the divisor. It should return a new list containing only the numbers from the original list that are divisible by the provided divisor.


def filter_number_divisible(input_list, devisor):
    result = []

    for num in input_list:
        if num % devisor == 0:
            result.append(num)

    return result


input_list = [15,10,10,24,23,45,13,19,33,9978980]
devisor = 5

check = filter_number_divisible(input_list, devisor)
print(check)