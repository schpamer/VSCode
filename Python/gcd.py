def convertFracs(l):
    print(l)
    for i in l:
        print(i)
        if l[i]l[i+] == 0:
            return l[i]
        else:
            x = l[i] % l[i+1]
            return convertFracs (x)
# import math

# def convertFracs(L):
#     print(L)
#     print(l[0])
#     #print (math.gcd(L[0]))
#     return

#p = gcd([4,8,12,24])
p = convertFracs([(1, 2), (1, 3), (1, 4)])
print(p)