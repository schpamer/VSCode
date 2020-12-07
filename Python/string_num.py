import string

# def alphabet_position(s):
#     di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))
#     print(di)
#     for i in di:
#         x = ([key for key in di.keys()][di])
#         y = " ".join(x)
#         print(x)s
#         #print (i, di[i])
#     return 


def alphabet_position(s):
    nums = [str(ord(x) - 96) for x in s.lower() if x >= 'a' and x <= 'z']
    return " ".join(nums)

p = alphabet_position("The sunset sets at twelve o' clock.")
print(p)