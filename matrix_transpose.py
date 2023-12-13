# Write a Python function that takes a square matrix (a list of lists representing a matrix where the number of rows is equal to the number of columns) and returns its transpose.



def transpose_matrix(matrix):
    # Using list comprehension to transpose the matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)

