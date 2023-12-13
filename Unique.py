# Write a Python function named find_unique that takes a list as an argument and returns a new list containing only the unique elements from the original list, preserving the order of elements. 

def find_unique_element(lst):
    unique_element = 0
    
    # XOR operation to find the unique element
    for num in lst:
        unique_element ^= num
    
    return unique_element

# Example list
input_list = [4, 2, 3, 4, 2, 3, 1]

unique = find_unique_element(input_list)
print(f"The unique element in the list is: {unique}")
