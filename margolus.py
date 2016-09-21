class MargolusRules(dict):

    KEY_MATCH = {
        0:  (0, 0, 0, 0), 1:  (1, 0, 0, 0), 2:  (0, 1, 0, 0), 3:  (1, 1, 0, 0),
        4:  (0, 0, 1, 0), 5:  (1, 0, 1, 0), 6:  (0, 1, 1, 0), 7:  (1, 1, 1, 0),
        8:  (0, 0, 0, 1), 9:  (1, 0, 0, 1), 10: (0, 1, 0, 1), 11: (1, 1, 0, 1),
        12: (0, 0, 1, 1), 13: (1, 0, 1, 1), 14: (0, 1, 1, 1), 15: (1, 1, 1, 1)
    }

    def __init__(self, iterable=None):
        if isinstance(iterable, (list, tuple)):
            for i, n in enumerate(iterable):
                k = MargolusRules.KEY_MATCH[i]
                v = MargolusRules.KEY_MATCH[n]
                self[k] = v


def update_neighborhood(i, j, grid, rules):
    m, n = grid.shape
    neighborhood = [
        (i % m, j % n),
        (i % m, (j+1) % n),
        ((i+1) % m, j % n),
        ((i+1) % m, (j+1) % n)]
    old_block = tuple(map(lambda ij: grid[ij], neighborhood))
    new_block = rules[old_block]
    for ij, val in zip(neighborhood, new_block):
        grid[ij] = val

def margolus_gen(grid, rules, parity, boundary=None):
    dij = int(bool(parity))
    m, n = grid.shape

    if boundary == "NO_WRAP":
        i_range = range(dij, m-dij, 2)
        j_range = range(dij, n-dij, 2)

    elif boundary == "H_WRAP":
        i_range = range(dij, m-dij, 2)
        j_range = range(-dij, n-dij, 2)

    elif boundary == "V_WRAP":
        i_range = range(-dij, m-dij, 2)
        j_range = range(dij, n-dij, 2)
    
    else:
        i_range = range(-dij, m-dij, 2)
        j_range = range(-dij, n-dij, 2)

    for i in i_range:
        for j in j_range:
            update_neighborhood(i, j, grid, rules)
