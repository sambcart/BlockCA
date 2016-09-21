import numpy as np
from margolus import MargolusRules

TRON_RULES     = MargolusRules((15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0))
HPP_RULES      = MargolusRules((0, 8, 4, 12, 2, 10, 9, 14, 1, 6, 5, 13, 3, 11, 7, 15))
BBM_RULES      = MargolusRules((0, 8, 4, 3, 2, 5, 9, 7, 1, 6, 10, 11, 12, 13, 14, 15))
CRITTERS_RULES = MargolusRules((15, 14, 13, 3, 11, 5, 6, 1, 7, 9, 10, 2, 12, 4, 8, 0))
BG1_RULES      = MargolusRules((0, 8, 4, 3, 2, 5, 9, 14, 1, 6, 10, 13, 12, 11, 7, 15))
BG2_RULES      = MargolusRules((0, 8, 4, 12, 2, 10, 9, 7, 1, 6, 5, 11, 3, 13, 14, 15))
ROTATE1_RULES  = MargolusRules((0, 2, 8, 12, 1, 10, 9, 11, 4, 6, 5, 14, 3, 7, 13, 15))
ROTATE2_RULES  = MargolusRules((0, 2, 8, 12, 1, 10, 9, 13, 4, 6, 5, 7, 3, 14, 11, 15))
ROTATE3_RULES  = MargolusRules((0, 4, 1, 10, 8, 3, 9, 11, 2, 6, 12, 14, 5, 7, 13, 15))
ROTATE4_RULES  = MargolusRules((0, 4, 1, 12, 8, 10, 6, 14, 2, 9, 5, 13, 3, 11, 7, 15))
STRING1_RULES  = MargolusRules((0, 1, 2, 12, 4, 10, 9, 7, 8, 6, 5, 11, 3, 13, 14, 15))
STRING2_RULES  = MargolusRules((0, 1, 2, 12, 4, 10, 6, 7, 8, 9, 5, 11, 3, 13, 14, 15))
DIAGSWAP_RULES = MargolusRules((0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15))
DUST_RULES     = MargolusRules((0, 4, 8, 12, 4, 12, 12, 13, 8, 12, 12, 14, 12, 13, 14, 15))

def initialize_grid_sparse_random(size):
    grid = np.zeros((size, size), dtype=np.uint8)
    num = (size*size / 400) + 1
    for _ in xrange(num):
        i, j = np.random.randint(size, size=2)
        grid[i, j] = 1
    return grid

def initialize_grid_random(size):
    return np.random.randint(2, size=(size, size), dtype=np.uint8)

def initialize_grid_normal(size):
    grid = np.zeros((size, size), dtype=np.uint8)
    num = (size*size / 10) + 1
    for _ in xrange(num):
        i = np.random.normal(size/2, size/15)
        j = np.random.normal(size/2, size/15)
        grid[int(i), int(j)] = 1
    return grid

def initialize_grid_points(size):
    grid = np.zeros((size, size), dtype=np.uint8)
    grid[size/3, size/3] = 1
    grid[size/3, 2*size/3] = 1
    grid[2*size/3, size/3] = 1
    grid[2*size/3, 2*size/3] = 1
    return grid

def initialize_grid_lines(size):
    grid = np.zeros((size, size), dtype=np.uint8)
    grid[size/3] = 1
    grid[:,size/3] = 1
    grid[2*size/3] = 1
    grid[:,2*size/3] = 1
    return grid
