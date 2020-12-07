def add_binary(a,b):
    c = a + b
    return print(format(c,'b'))

add_binary(51,12)
#add_binary(2,2)


def add_binary(a,b):
    return bin(a+b)[2:]

    def add_binary(a, b):
    return format(a + b, 'b')