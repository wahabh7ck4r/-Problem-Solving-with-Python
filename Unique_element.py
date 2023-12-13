# Create a function that returns all unique elements from a list.

def unique_element_in_list(input_list):
    unique_element = set(input_list)

    return  unique_element

ls = ['python', 'hello', 22 , 11 , 22 ,'python']
chcek = unique_element_in_list(ls)
print(chcek)

