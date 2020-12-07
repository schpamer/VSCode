
def find_outlier(nums):
    
    odds = ([i for i in nums if i % 2 != 0])
    evens = ([i for i in nums if i % 2 == 0])

    return odds[0] if len(odds) < len(evens) else evens[0]


ans = find_outlier([2, 4, 6, 8, 10, 3])
print(ans)

#odd = [i for i in x if i % 2 != 0]
#    even = [i for i in x if i % 2 == 0]


#num = int(input("Enter a number: "))
#if (num % 2) == 0:
#   print("{0} is Even".format(num))
#else:
#   print("{0} is Odd".format(num))
#
#   myNum = 21
#if myNum & 1 == 1:
#    print("The number is odd number.")
#else:
#    print("The number is even number."