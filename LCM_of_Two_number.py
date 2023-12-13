# write a program to check LCM of two number enter by the user.

num1 = int(input("Enter a first number:\n"))
num2 = int(input("Enter a second number:\n"))

maxnum = max(num1,num2)

while True:
    if maxnum%num1==0 and maxnum%num2==0:
        break
    maxnum +=1

print(f"The LCM of {num1} and {num2} is : {maxnum}")

