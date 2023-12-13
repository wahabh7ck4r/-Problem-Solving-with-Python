# Write a Python program that includes a function for converting temperatures between Celsius and Fahrenheit. The program should have two functions, celsius_to_fahrenheit and fahrenheit_to_celsius, each taking a temperature as input and returning the converted temperature.


def celsius_to_fahrenheit(celsius):
    frh_tem = (celsius * 9/5) + 32 #usnig formula
    return frh_tem

def fahrenheit_to_celsius(fahrenheit):
    cls_tem = (fahrenheit - 32) * 5/9 #using formula
    return cls_tem

celsius_temperature = 30
print(f"{celsius_temperature} Celsius in Fahrenheit: {celsius_to_fahrenheit(celsius_temperature)}")

fahrenheit_temperature = 86
print(f"{fahrenheit_temperature} Fahrenheit in Celsius: {fahrenheit_to_celsius(fahrenheit_temperature)}")

