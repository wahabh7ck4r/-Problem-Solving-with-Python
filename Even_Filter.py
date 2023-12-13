# Write a program that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.


def Even_filter():
    while True:   
        num_len = input("How many number you want to enter in a list: ")
        if num_len.isdigit():
            num_len = int(num_len)
            num_list = [int(input(f"Enter the {i} num: ")) for i in range(num_len)]
            break
        else:
            print("Enter only integer")

    even_num = []

    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            even_num.append(num_list[i])
            
    return even_num


result = Even_filter()
print(f"even number in the list: {result} ")
