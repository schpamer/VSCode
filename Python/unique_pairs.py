from math import factorial

def projectPartners(n):
    x = factorial(n) / (factorial(2) * (factorial(n - 2)))
    return x

p = projectPartners(4)
print(p)