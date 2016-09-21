import matplotlib.pyplot as plt
from utils import *
from margolus import *

def main():
    SIZE = 130
    GRID = initialize_grid_sparse_random(SIZE)
    PARITY = 0
    
    fig = plt.figure()
    img_plot = plt.imshow(GRID, interpolation="nearest", cmap=plt.cm.gray)
    plt.show(block=False)
    
    while True:
        margolus_gen(GRID, BBM_RULES, PARITY, boundary="NO_WRAP")
        img_plot.set_data(GRID)
        fig.canvas.draw()
        PARITY = 1 - PARITY

if __name__ == "__main__":
    main()
