from functools import lru_cache

@lru_cache(maxsize=1000)
def next_smaller(x):
    x=str(x)   
    for i in range(2,len(x)+1):
        p=sorted(x[-i+1:])[::-1]
        for j in range(len(p)):
            if p[j]<x[-i]:
                s=x[:-i]+p[j]
                p.pop(j)
                p.append(x[-i])
                s+="".join(sorted(p)[::-1])
                if s[0]=="0":
                    return -1
                else:
                    return int(s)
                    
    return -1

#Returns next bigger number or -1 if not possible (simple change from above function)    
def next_bigger(x):
    x=str(x)   
    for i in range(2,len(x)+1):
        p=sorted(x[-i+1:])
        for j in range(len(p)):
            if p[j]>x[-i]:
                s=x[:-i]+p[j]
                p.pop(j)
                p.append(x[-i])
                s+="".join(sorted(p))
                return s
                    
    return -1
                 
#Main        
x = next_smaller(907)
print("Number",x)
print("Next Smaller",next_smaller(x))
print("Next Bigger", next_bigger(x))


#not fast enough
# import itertools
# from functools import lru_cache

# @lru_cache(maxsize=1000)
# def smaller_number(number):
#     """
#     in: positive integrer
#     out: one step smaller integrer containing same digits or -1 (leading zeros not allowed)
#     """
#     # make sorted list of possible combinations with digits in given number
#     digit_list = [digit for digit in str(number)]
#     combinations = sorted(set(itertools.permutations(digit_list)))
#     smallness_number = combinations.index(tuple(digit_list))

#     # check if given number is the smallest possible number without leading zeros
#     if smallness_number == 0 or combinations[smallness_number-1][0] == "0": 
#         return -1
#     else:
#         return int("".join(combinations[smallness_number-1]))
        

# number = smaller_number(1234567908)
# print(number, type(number))