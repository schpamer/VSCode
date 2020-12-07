
# from collections import Counter

# def check_dups(l):
#     counts = Counter()
#     for cell in l:
#         if cell != 0: counts[cell] += 1
#         if cell > 9 or counts[cell] > 1: return False
#     return True

# def validSolution(grid):
#     if len(grid) != 9: return False
#     if sum(len(row) == 9 for row in grid) != 9: return False
#     for row in grid:
#         if not check_dups(row): return False
#     return True
# import itertools

# def validSolution(matrix):
#     squares = []
#     for i in range(0, 3):
#             for j in range(0, 3):
#                 square = list(itertools.chain(row[j:j+3] for row in matrix[i:i+3]))
#                 squares.append(square)
#                 bad_squares = [square for square in squares if not sudoku_ok(square)] 
#     numbers = set(range(1, len(matrix) + 1))
#     if (any(set(row) != numbers for row in matrix) or
#         any(set(col) != numbers for col in zip(*matrix))) :
        
#         return False
#     return True

import numpy as np

def validSolution(m):
    grid = np.array([[int(i) for i in line] for line in m])
    #print(grid)
    #grid = np.array([[int(i) for i in line] for line in grid.split()])
    #print(grid)
    """ Return True if grid is a valid Sudoku square, otherwise False. """
    for i in range(9):
        # j, k index top left hand corner of each 3x3 tile
        j, k = (i // 3) * 3, (i % 3) * 3
        if len(set(grid[i,:])) != 9 or len(set(grid[:,i])) != 9\
                   or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
            return False
    return True


# m = """ 123456789
#         839654127
#         672918543
#         496185372
#         218473956
#         753296481
#         367542819
#         984761235
#         521839764"""

# m = ([
#     [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#     [2, 3, 4, 5, 6, 7, 8, 9, 1],
#     [3, 4, 5, 6, 7, 8, 9, 1, 2],
#     [4, 5, 6, 7, 8, 9, 1, 2, 3],
#     [5, 6, 7, 8, 9, 1, 2, 3, 4],
#     [6, 7, 8, 9, 1, 2, 3, 4, 5],
#     [7, 8, 9, 1, 2, 3, 4, 5, 6],
#     [8, 9, 1, 2, 3, 4, 5, 6, 7],
#     [9, 1, 2, 3, 4, 5, 6, 7, 8]
# ])

m = ([
    [5, 3, 4, 6, 7, 8, 9, 1, 2], 
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

print(m)
if validSolution(m):
    print('grid valid')
else:
    print('grid invalid')
# if validSolution(grid):
#     print('grid valid')
# else:
#     print('grid invalid')

   
    


# """ check quadrants """
#     qsize = int(shouldBe**0.5)

#     """ iterate through quadrants """
#     for i in range(qsize):
#         for j in range(qsize):
#             toCheck = {i:0 for i in range(1, shouldBe+1)}

#             """ iterate through single quadrant """
#             for row in range(i*qsize, (i+1)*qsize):
#                 for col in range(j*qsize, (j+1)*qsize):
#                     tmp = su[row][col]
#                     toCheck[tmp] += 1

#             if not check(toCheck):
#                 return False
#     return True


# m = validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ])
