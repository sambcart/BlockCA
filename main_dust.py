import matplotlib.pyplot as plt
from utils import *
from margolus import *

def main():
    SIZE = 130
    GRID = initialize_grid1(SIZE)
    PARITY = 0
    INCR = 0

    fig = plt.figure()
    img_plot = plt.imshow(GRID, interpolation="nearest", cmap=plt.cm.gray)
    plt.show(block=False)

    while INCR < 2000:
        margolus_gen(GRID, DUST_RULES, PARITY, boundary="H_WRAP")
        img_plot.set_data(GRID)
        fig.canvas.draw()
        PARITY = 1 - PARITY
        INCR += 1

if __name__ == "__main__":
    main()
