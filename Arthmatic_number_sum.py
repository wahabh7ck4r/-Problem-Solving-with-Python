# Calculate the sum of the first 20 terms of the arithmetic sequence where the first term (a₁) is 3 and the common difference (d) is 7.
# Hint: The formula to find the sum of the first n terms of an arithmetic sequence is Sₙ = n/2 * [2a₁+(n - 1)*d]


def sum_of_arthmethic_num(a,d,n):
    Sn = n/2 * (2*a + (n-1)*d)
    Sn = int(Sn)

    return Sn

a = 3
d = 7
n = 20 

check = sum_of_arthmethic_num(a,d,n)

print(check)