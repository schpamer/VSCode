from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)

# ts = [50, 55, 56, 57, 58] 
# p = choose_best_sum(163, 3, ts)
# ys = [91, 74, 73, 85, 73, 81, 87] 
# p = choose_best_sum(230, 3, ys)
xs = [50] 
p = choose_best_sum(163, 3, xs)
print(p)