def high_and_low(nums):
    
    T2 = list(map(int , nums.split(' ')))
    return "%i %i" % (max(T2), min(T2))

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
