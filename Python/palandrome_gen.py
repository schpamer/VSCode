def palindrome(n, c): 
    print (n, c);
    print(c[0])
    print(c)
    print(c[-1-n%2::-1])
    print((c[-1-n%2::-1]).center(n,c[0]))
    return (c+(c[-1-n%2::-1])).center(n,c[0])

#def palindrome(n, s): lambda n,s:(s+s[-1-n%2::-1]).center(n,s[0]); return (n,s)
# print(len('def palindrome(n,c):exit(c+(c[-1-n%2::-1])).center(n,c[0])'))
# print(len('def'))
# print(len('palindrome'))
# print(len('return'))
# print(len('center'))
# print(3+10+6+6)
#print(c[0])
# def palindrome(n, c): 
#         x=(c[-2::-1]);
#         print(x)
#         y= (c+x);
#         print(y)
#         e = 0
#         while n >= e:
#             b = (y[-2::-1])
#             y = (y+b)
#             print(y)
#             e =(len(y))
#         return y
    

# a = len('def palindrome(n, c): x=(c[-2::-1]); y= (c+x); return y')
# print(a)


# ab -> ba
# ab -> a
# aba   complete                [a,b]
# aba -> aba
# aba -> ba
# abba -> abba compkete 4
# abba -> abba
# abba -> bba
# abba -> abbabba complete 7
# abbabba -> abbabba
# abbabba -> bbabba
# abbabba -> abbabbabbabba
#p=palindrome(3,"ab")
#p = palindrome(51,"abcdefghijklmnopqrstuvwxyz")
#p=palindrome(1,  "a")
p = palindrome(10, "ab")

#print(len(p))
print(p)
print(len(p))

# # Skip single-digit inputs
#     if num // 10 == 0:
#         return False

#x=(c[-2::-1]); y= (c+x); return y if len(y) == n else: return c