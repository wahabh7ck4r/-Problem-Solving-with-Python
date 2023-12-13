# Write a Python function to find the factorial of a number.

def factorial(num):
    if num == 1 or num == 0: 
        return 1
    
    return num * factorial(num -1)

num = int(input("Enter the number to find the factorail: "))

check = factorial(num)
print(f"The factorial of {num} is : {check}")