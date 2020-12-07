# from itertools import combinations_with_replacement

# def find_all(n,m):
#     r = range(1,n)
#     result = [seq for i in range(0,len(r),1) for seq in combinations_with_replacement(r, m) if sum(seq) == 27]
#     print(result)
#     result = set(result)
#     x = (len(result))
#     y = (min(result))
#     y = int(('{}{}{}'.format(*y)))
#     z = (max(result))
#     z = int(('{}{}{}'.format(*z)))
#     q = [x,y,z]
#     print(q)
#    return q
from itertools import combinations_with_replacement

def find_all(s, d):
    combination = combinations_with_replacement(list(range(1, 10)), d)
    target = [''.join(str (x) for x in list(comb)) for comb in combination if sum(comb) == s]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]

p = find_all(84, 4)
print(p)
# from itertools import combinations

# def find_all(n, s):
#     print (n, s)
#     result = [seq for i in range(0,n) for seq in combinations(n, s) if sum(seq) == n]
#     y = (set(result))
#     print(y)
#     return y

# find_all(10, 3)


# from itertools import combinations
# n = 10
# dig = 3
# x = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
# y = list(combinations(range(n),dig))
# z = list(map(sum, y))
# print(y)
# print(z)
# print(y[13])
# print(sum(y[13]))


# from itertools import combinations_with_replacement

# def find_all(n,m):
#     result = set([seq for i in range(0,len(range(1,n)),1) for seq in combinations_with_replacement(range(1,n), m) if sum(seq) == n])
#     x = (len(result))
#     y = (min(result))
#     y = int(('{}{}{}'.format(*y)))
#     z = (max(result))
#     z = int(('{}{}{}'.format(*z)))
#     q = [x,y,z]
#     print(q)
#     return q

# find_all(10,3)

# tup = int(str((1, 1, 8)))
# x = ''.join(tup)
# print(x)

# from itertools import combinations_with_replacement

# def find_all(n,m):
#     result = set([seq for i in range(0,len(range(1,n)),1) for seq in combinations_with_replacement(range(1,n), m) if sum(seq) == n])
#     y = ''.join(map(str,result))
#     print(y)
#     #print(result)
#     y = [len(result),''.join(str(min(result))),''.join(str(max(result)))]
#     print(y)
#     #print(min(result))
#     #print(max(result))
#     #print(result)
#     return

# find_all(10,3)