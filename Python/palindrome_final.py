# # def palindrome(n,c): return (c+(c[-2-&1::-1])).center(n,c[0])
# # p = palindrome(51, "abcdefghijklmnopqrstuvwxyz")
# # print(p)
# # print(len(p))

# #c = "abcdefghijklmnopqrstuvwxyz"
# c = "ab"
# n = 2
# print(c)
# #x = c[:-1]
# x= c.reverse()
# print(x)
# print(c+x)
# # print(c+x)
# # y = (c+x)
# # print(y.center(n,c[0]))
# # y = (y.center(n,c[0]))
# # print(len(y))
# print(n%2)
# print(c[0])
# print(c[-1])
# print(c[-2])
# z = (c+(c[-1-n%2::-1])).center(n,c[0])
# print(z)


# # n = 10
# # print(-(n&1))

# # n = 5
# # print(-(n&1))

palindrome=lambda n,s:(s+s[-1-n%2::-1]).center(n,s[0])

p = palindrome(2, [937, 113])
print(p)

#print(len('palindrome = lambda n,s:(s+s[-1-n%2::-1]).center(n,s[0])'))