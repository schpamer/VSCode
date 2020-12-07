import math

def is_square(integer):
    root = math.sqrt(integer)
    print(root)
    return print(integer == int(root + 0.5) ** 2)

is_square(81)
