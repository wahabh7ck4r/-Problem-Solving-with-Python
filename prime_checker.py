# Write a Python function is_prime() that takes an integer as an argument and returns True if the number is a prime number, and False otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.


def is_prime(num):

    if num <= 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True



chcek_num = int(input("Enter a number to check is it prime or not: "))
result = is_prime(chcek_num)
print(result)