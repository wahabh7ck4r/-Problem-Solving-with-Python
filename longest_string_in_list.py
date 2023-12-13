# Write a Python function that takes a list of strings as input and returns the longest string from the list. If there are multiple strings with the same longest length, return the first one encountered in the list.


# first method 
def find_longest_string(ls):
    len_ls = []

    for i in range(len(ls)):
        word = ls[i]
        word = word.strip()
        len_ls.append(len(word))

    max_valuse = max(len_ls)
    max_index = len_ls.index(max_valuse)
    
    longest_str = ls[max_index]

    return longest_str 


ls = ['apple', 'banana', 'kiwi', 'orange']

check = find_longest_string(ls)
print(check)


# second method 

def find_longest_string_2(ls):
    longest_str = max(ls, key=len)
    return longest_str


ls = ['apple', 'banana', 'kiwi', 'orange']

check2 = find_longest_string(ls)
print(check2)
