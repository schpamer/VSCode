from itertools import cycle


def pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])

def encode(plaintext, nrails):
    p = pattern(nrails)
    return ''.join(sorted(plaintext, key=lambda i: next(p)))

def decode(ciphertext, nrails):
    p = pattern(nrails)
    indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
    result = [''] * len(ciphertext)
    for i, c in zip(indexes, ciphertext):
        result[i] = c
    return ''.join(result)

p = decode("WECRLTEERDSOEEFEAOCAIVDEN",3)
print(p)

#WECRLTEERDSOEEFEAOCAIVDEN