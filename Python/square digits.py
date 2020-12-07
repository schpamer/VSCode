def square_digits(num):
    y = ''
    for ch in str(num):
        y += str(int(ch)**2)
    return int(y)


p = square_digits(9119)
print(p)
