# Write a Python function called safe_divide that takes two numbers as input and performs division. However, this function should handle the scenario where division by zero occurs using a try and except block.  


def safe_divide(numerator , denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print("denominator must be grater then zero")
        return ""
    
    return result

numerator = 88
denominator =0

check = safe_divide(numerator, denominator)
print(check)