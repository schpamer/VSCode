# def natural(input):
#     x = 0
#     n = 
#     if (input % 3 ==0) or (input % 5 == 0):
#             sum += input
#     return print(sum)

# natural(10)


# import numpy as np

# def natural(input):
#     x = np.arange(1, input)
#     n= x[(x % 3 == 0) | (x % 5 == 0)]
#     return print((n.sum()))

# natural(10)
def natural(input):
    
    return sum(x for x in range(input) if x % 3 == 0 or x % 5 == 0)

print(natural(900))