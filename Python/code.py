import codecs

def rot(plain):
    x = codecs.encode(plain, 'rot13')
    return x

rot('This is my first ROT13 excercise!')
print(dir(codecs))


