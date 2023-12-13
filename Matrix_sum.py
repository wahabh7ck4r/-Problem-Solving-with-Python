# write a program to sum two matrix


def matrix(m,n):
    O = []
    for i in range(m):
        row = []
        for j in range(n):
            vl = int(input(f"Enter a value for A{i}{j}: "))
            row.append(vl)
        O.append(row)
    return O

def sum_matrix(A,B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

m = int(input("Enter the value m\n"))
n = int(input("Enter the value n\n"))


A = matrix(m,n)
B = matrix(m,n)

s = sum_matrix(A,B)
print(s)