import os
import datetime

import numpy as np
import open3d as o3d


def load_xyz_open3d(name, path):
    final_path = path + name + '.xyz'
    if os.path.isfile(final_path):
        xyz = o3d.io.read_point_cloud(final_path)
        o3d.visualization.draw_geometries([xyz], point_show_normal=True, width=1080, height=720, )
    else:
        print("%s DOESN'T EXIST!!" % final_path)


def points_in_circum(r, origin, n=100):
    x, y, z = origin
    points = [((np.cos(2*np.pi/n*I)*r+x), y, np.sin(2*np.pi/n*I)*r+z) for I in range(0,n+1)]

    return points


def rotate_around_point(input, origin, direction):
    x_axis, y_axis, z_axis = (0, 0, 0)

    if direction[0] != 0:
        if direction[1] == 0:
            x_axis = np.deg2rad(90)
        else:
            x_axis = np.tan(direction[1] / np.sqrt(direction[0] ** 2 + direction[1] ** 2))
    else:
        x_axis = 0

    y_axis = 0

    if direction[2] != 0:
        if direction[1] == 0:
            z_axis = np.deg2rad(90)
        else:
            z_axis = np.tan(direction[1] / np.sqrt(direction[2] ** 2 + direction[1] ** 2))
    else:
        z_axis = 0

    pitch = x_axis
    yaw = y_axis
    roll = z_axis

    x_rotation = [[np.cos(pitch), -np.sin(pitch), 0],
                  [np.sin(pitch), np.cos(pitch), 0],
                  [0, 0, 1]]
    y_rotation = [[np.cos(yaw), 0, np.sin(yaw)],
                  [0, 1, 0],
                  [-np.sin(yaw), 0, np.cos(yaw)]]
    z_rotation = [[1, 0, 0],
                  [0, np.cos(roll), -np.sin(roll)],
                  [0, np.sin(roll), np.cos(roll)]]
    r_total = np.matmul(np.matmul(x_rotation, y_rotation), z_rotation)

    output = np.matmul(r_total, input)
    return output

def main():
    origin = [0, 0, 0]
    points = points_in_circum(40, origin)
    rotated_points = []
    for point in points:
        rotated_points.append(rotate_around_point(point, origin, [0, 1, 1]))

    DIR = os.getcwd() + '\\xyz/'
    DIR = DIR.replace('\\', '/')
    amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    with open(
            DIR + "test_rotation.xyz",
            'w') as f:
        for point in rotated_points:
            pointz = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2]) + '\n'
            f.write(pointz)
        f.close()

    model = o3d.io.read_point_cloud(DIR + "test_rotation.xyz")
    print(model)
    o3d.visualization.draw_geometries([model], width=1080, height=720)


if __name__ == '__main__':
    main()
