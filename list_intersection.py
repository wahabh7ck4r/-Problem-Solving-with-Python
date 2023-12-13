# Write a Python function called find_intersection that takes two lists of integers, list1 and list2, and returns a new list containing the intersection of elements, i.e., the elements that are common to both lists without any duplicates.

def find_intersection(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
        
    result = sorted(result)

    return f"The intersection of {list1} and {list2} is: {result}"  


input_list_1 = [1, 2, 3, 4, 5]
input_list_2 = [3, 4, 5, 6, 7, 9]

check = find_intersection(input_list_1,input_list_2)
print(check)