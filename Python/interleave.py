from itertools import zip_longest

def interleave(*args):
    x = [val for pair in zip_longest(*args) for val in pair]
    print(x)
    return x


#p = interleave([])
p = interleave([1, 2, 3], ["c", "d", "e"])
#p = interleave([1, 2, 3], [4, 5])
print(p) 

