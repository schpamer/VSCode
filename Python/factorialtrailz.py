def Trailing_Zeroes(n):
    assert n >= 0, n
    zeros = 0
    q = n

    while q:
        q //= 5
        zeros += q

    return zeros

zeros = Trailing_Zeroes(15)
print(zeros)