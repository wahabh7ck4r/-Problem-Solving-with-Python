# Write a Python function called merge_lists_alternately that takes two lists as input and returns a new list containing elements merged alternately from the input lists.

def merge_lists_alternately(list1, list2):
    merged_list = []
    min_len = min(len(list1), len(list2))  # Find the minimum length among the two lists

    for i in range(min_len):  # Iterate till the minimum length
        merged_list.append(list1[i])  # Append element from list1
        merged_list.append(list2[i])  # Append element from list2

    # If one list is longer than the other, add remaining elements from that list
    merged_list.extend(list1[min_len:] if len(list1) > len(list2) else list2[min_len:])
    return merged_list

# Test case
input_list1 = [1, 2, 3]
input_list2 = ['a', 'b', 'c', 'd']
print(merge_lists_alternately(input_list1, input_list2))
