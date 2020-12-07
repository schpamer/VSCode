# import primefac
# import sys

# def prime_decomp(input):
#     n = int( input )
#     x = list( primefac.factorint(n) )
#     print (''.join(map(str, x)))
#     return

# prime_decomp(86240)





# #86240 should return "(2**5)(5)(7**2)(11)"
# from collections import Counter
# from sympy.ntheory import primefactors, factorint, isprime

# def prime_factors(n):
#     print(n)
#     #print (primefactors(n)[-1])
#     print(sorted(factorint(n).items()))
#     return
    # """Returns all the prime factors of a positive integer"""
    # factors = []
    # d = 2
    # while n > 1:
    #     while n % d == 0:
    #         factors.append(d)
    #         n /= d
    #     d = d + 1
    #     if d*d > n:
    #         if n > 1: factors.append(n)
    #         break
    
    #!python

# import primefac
# import sys

# n = int( sys.argv[1] )
# factors = list( primefac.primefac(n) )
# print '\n'.join(map(str, factors))
    
    # result = ""        
    # for i in factors:
    #     result += "({}**{})".format(i, amounts[i]) if amounts[i] !=1 else "({})".format(i)
    # return result
def prime_factors(n):
        i = 2
        factors = []
        count = 0                           #added to test optimization
        while i * i <= n:
            count += 1                      #added to test optimization
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return print(factors, f'count: {count}')   #print with (count added)

pfs = prime_factors(86240)
# largest_prime_factor = max(pfs) # The largest element in the prime factor list
# print(pfs)
# x = pfs.count(2)
# print(x)
# y = pfs.count(5)
# print(y)
# c2 = Counter(pfs)
# print(c2)