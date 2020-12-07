import itertools
from functools import lru_cache

@lru_cache(maxsize=1000)
def next_smaller(someInt):

        num = str(someInt)
        listOfNums = set([int(''.join(nums)) for nums in itertools.permutations(num, len(num))])
        listOfNums = sorted(list(listOfNums))
        x =(listOfNums[listOfNums.index(someInt)-1])
        y =(listOfNums[listOfNums.index(someInt)])
        if x < y:
            print(x)
        else:
            print(-1)
        
next_smaller(1234567890)

#22439665351571356161112233345555666679   22439665351571356159766666555433322111

# num = list('1222')
# #start from the last digit
# index_to_swap = len(num) - 1
# #iterate from 2nd last digit backwards till the start.
# # Note that range is right-exclusive, so you need to write -1 to actually reach 0 in this case.
# for i in range(len(num) - 2, -1, -1):
#     #if you find a smaller digit while going in reverse
#     if num[i] < num[index_to_swap]:
#         # then swap in place.
#         num[index_to_swap], num[i] = num[i], num[index_to_swap]
#         print(num)
#         break
#     else:
#         # otherwise, this digit is same or larger from right to left, use this digit now for consideration
#         index_to_swap = i
# else:
#     # this is a for: else shortcut syntax, if for loop ever runs to completion without "break", This part executes
#     print('its already largest')
