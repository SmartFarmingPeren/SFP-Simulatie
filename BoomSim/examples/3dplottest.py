import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

factor = 100
N = 500


def main():
    Draw_3D_Test_Plot()






def Translate(array):
    i = 0
    for numbers in array:
        array[i] = array[i] * factor
        i += 1

    return array

def Draw_3D_Test_Plot():
    x = Translate(np.random.rand(N))
    y = Translate(np.random.rand(N))
    z = Translate(np.random.rand(N))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim(factor)
    ax.set_ylim(factor)
    ax.set_zlim(factor)

    ax.plot(x, y, z, label="Point Cloud test")
    ax.legend()

    plt.show()


if __name__ == '__main__':
    main()