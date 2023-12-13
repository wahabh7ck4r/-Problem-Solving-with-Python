# Write a Python function called merge_sorted_arrays that takes in two sorted lists of integers, arr1 and arr2, and merges them into a single sorted list.

def merge_sorted_arrays(arr1, arr2):
    sort_arr_1 = sorted(arr1)
    sort_arr_2 = sorted(arr2)
    
    merge_array = sorted(set(arr1 + arr2))

    return merge_array


arr1 = [1,2,4,5,2,1]
arr2 = [6,7,9,5,2]

check = merge_sorted_arrays(arr1,arr2)
print(check)


