# Write a Python function that takes a list of integers as input and returns the count of prime numbers in the list


def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True


def Prime_counter(input_list):
    result = 0

    for num in input_list:
        if is_prime(num):
            result += 1

    return f"The total prime number in the given list are: {result}"



ls = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
check = Prime_counter(ls)
print(check)