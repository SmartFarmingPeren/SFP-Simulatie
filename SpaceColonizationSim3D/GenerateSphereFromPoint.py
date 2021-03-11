import os
import datetime

import numpy as np
import open3d as o3d


def sphere(shape, radius, position):
    # assume shape and position are both a 3-tuple of int or float
    # the units are pixels / voxels (px for short)
    # radius is a int or float in px
    semisizes = (radius,) * 3

    # genereate the grid for the support points
    # centered at the position indicated by position
    grid = [slice(-x0, dim - x0) for x0, dim in zip(position, shape)]
    position = np.ogrid[grid]
    # calculate the distance of all points from `position` center
    # scaled by the radius
    arr = np.zeros(shape, dtype=float)
    for x_i, semisize in zip(position, semisizes):
        # this can be generalized for exponent != 2
        # in which case `(x_i / semisize)`
        # would become `np.abs(x_i / semisize)`
        arr += (x_i / semisize) ** 2

    # the inner part of the sphere will have distance below 1
    return arr <= 1.0



# create a rotated circle in a 3d space
def main():
    origin = [0, 0, 0]
    # create circle
    points = sphere((256, 256, 256), 10, (127, 127, 127))

    # save circle
    DIR = os.getcwd() + '\\xyz/'
    DIR = DIR.replace('\\', '/')
    amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    with open(
            DIR + "test_rotation.xyz",
            'w') as f:
        for point in points:
            pointz = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2]) + '\n'
            f.write(pointz)
        f.close()

    # show circle
    model = o3d.io.read_point_cloud(DIR + "test_rotation.xyz")
    print(model)
    o3d.visualization.draw_geometries([model], width=1080, height=720)


if __name__ == '__main__':
    main()
