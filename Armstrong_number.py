# write a program to enter a number by the user and check is it an amrstrong number or not?

def armstrong():
    num = int(input("Enter the numbe: "))
    order = len(str(num))
    sm = 0
    cp_num = num
    while(num>0):
        digit = num%10
        sm += digit ** order
        num = num //10

    if(sm == cp_num):
        print(f"{cp_num} is an armstrong number")
    else:
        print(f"{cp_num} is not a armstrong number.")


armstrong()