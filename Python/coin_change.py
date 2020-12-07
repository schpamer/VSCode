# from itertools import combinations, permutations


# def count_change(money, coins):
     
#     perm = permutations(coins) 
#     print(perm)
# # Print the obtained permutations 
#     for i in list(perm): 
# 	    print (i)
        

# c = count_change(4, [1,2])
# #print(c)
#%%
def solve(n, coins, k):
    """
    Solution for count_change
    :param n: money
    :param coins: List of coins.
    :param k: coins[k]
    :return: Count of combinations.
    """

    # print("n: %d, k: %d" % (n, k))
    if k < 0 or n < 0:
        return 0

    if n == 0:  # Change for 0 is only empty one.
        return 1

    # print("  n: %d, k: %d" % (n, k - 1))
    # print("  n: %d, k: %d" % (n - coins[k], k))

    # solve(n, coins, k - 1) -> Count of money without coins[k]
    # solve(n - coins[k], coins, k) -> Count of (money - coins[k]) with coins[k]
    count = solve(n, coins, k - 1) + solve(n - coins[k], coins, k)

    # print("Count: %d" % count)
    return count


def count_change(money, coins):
    return solve(money, coins, len(coins) - 1)

#c = count_change(4, [1,2])
#c = count_change(10, [5,2,3])
c = count_change(11, [5,7])
print(c)

# %%
