if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from utils import *
    from margolus import *

    SIZE = 100
    GRID = initialize_grid_lines(SIZE)
    PARITY = 0

    fig = plt.figure()
    img_plot = plt.imshow(GRID, interpolation="nearest", cmap=plt.cm.gray)
    plt.show(block=False)

    while True:
        margolus_gen(GRID, TRON_RULES, PARITY)
        #img_plot.set_data(GRID)
        img_plot.set_data(PARITY - GRID)
        fig.canvas.draw()
        PARITY = 1 - PARITY
