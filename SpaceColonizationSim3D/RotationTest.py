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


# Creates a circle around a point
def points_in_circum(r, origin, n=100):
    x, y, z = origin
    points = [[(np.cos(2 * np.pi / n * I) * r + x), y, np.sin(2 * np.pi / n * I) * r + z] for I in range(0, n + 1)]

    return points


# Rotate a point(input) around another point(origin). Does not yet work with propositions, given a direction (1, 0,
# 0.5) for example the code should give a z_rotation of less than 90 but this is not the case.
def rotate_around_point(input, origin, direction, x_axis=0, y_axis=0, z_axis=0):
    x_axis, y_axis, z_axis = calculate_axes(direction)

    roll = x_axis
    yaw = y_axis
    pitch = z_axis

    # This math is from: https://en.wikipedia.org/wiki/Rotation_matrix
    x_rotation = [[1, 0, 0],
                  [0, np.cos(pitch), -np.sin(pitch)],
                  [0, np.sin(pitch), np.cos(pitch)]]
    y_rotation = [[np.cos(yaw), 0, np.sin(yaw)],
                  [0, 1, 0],
                  [-np.sin(yaw), 0, np.cos(yaw)]]
    z_rotation = [[np.cos(roll), -np.sin(roll), 0],
                  [np.sin(roll), np.cos(roll), 0],
                  [0, 0, 1]]
    r_total = np.matmul(np.matmul(x_rotation, z_rotation), y_rotation)

    # Removing origin(middle point) from the input(point of the circle) to remove unwanted behevior
    translated_input = [input[0] - origin[0], input[1] - origin[1], input[2] - origin[2]]

    output = np.matmul(r_total, translated_input)

    return output + origin


# calculate the different axis
# probably something wrong with this.
def calculate_axes(direction):
    if direction[0] != 0:
        x_axis = np.tan(direction[0] / np.sqrt(direction[0] ** 2 + direction[1] ** 2))
    else:
        x_axis = 0

    if direction[0] != 0:
        if direction[2] != 0:
            y_axis = np.tan(direction[2] / np.sqrt(direction[0] ** 2 + direction[2] ** 2))
        else:
            y_axis = np.deg2rad(90)
    else:
        y_axis = 0

    if direction[2] != 0:
        z_axis = np.tan(direction[2] / np.sqrt(direction[2] ** 2 + direction[1] ** 2))
    else:
        z_axis = 0

    return x_axis, y_axis, z_axis


# The z coordinate isn't implemented yet.
def rotateZ3D(theta, input):
    sinTheta = np.sin(np.deg2rad(theta))
    cosTheta = np.cos(np.deg2rad(theta))
    output = input
    output[0] = input[0] * cosTheta - input[1] * sinTheta
    output[1] = input[1] * cosTheta - input[0] * sinTheta
    return output


# The z coordinate isn't implemented yet.
def rotateX3D(theta, input):
    sinTheta = np.sin(np.deg2rad(theta))
    cosTheta = np.cos(np.deg2rad(theta))
    output = input
    output[0] = input[1] * cosTheta - input[2] * sinTheta
    output[1] = input[2] * cosTheta - input[1] * sinTheta
    return output


# The z coordinate isn't implemented yet.
def rotateY3D(theta, input):
    sinTheta = np.sin(np.deg2rad(theta))
    cosTheta = np.cos(np.deg2rad(theta))
    output = input
    output[0] = input[0] * cosTheta - input[2] * sinTheta
    output[1] = input[2] * cosTheta - input[0] * sinTheta
    return output


def view_models(model_names):
    models = []
    for name in model_names:
        models.append(o3d.io.read_point_cloud(name))
    o3d.visualization.draw_geometries(models, width=1080, height=720, mesh_show_back_face=False)


def view_pointclouds(pcds):
    o3d.visualization.draw_geometries(pcds, width=1080, height=720, mesh_show_back_face=False)


# create a rotated circle in a 3d space
def main():
    origin = [0, 0, 0]
    # create circle
    points = points_in_circum(40, origin)

    # rotate circle
    rotated_points = []
    for point in points:
        rotated_points.append(rotate_around_point(point, origin, [0, 0, 0], np.deg2rad(102), np.deg2rad(60), np.deg2rad(20)))

    # save circle
    DIR = os.getcwd() + '\\xyz/'
    DIR = DIR.replace('\\', '/')
    # amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    # with open(
    #         DIR + "test_rotation.xyz",
    #         'w') as f:
    #     for point in rotated_points:
    #         pointz = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2]) + '\n'
    #         f.write(pointz)
    #     f.close()

    # show circle
    branches = o3d.io.read_point_cloud("xyz/base/gen_1_18_03_base.xyz")
    leaves = o3d.io.read_point_cloud(DIR + 'leaves_05_03.xyz')
    leaves.paint_uniform_color((.1, .8, .1))
    print(branches)
    o3d.visualization.draw_geometries([branches], width=1080, height=720, mesh_show_back_face=False)


if __name__ == '__main__':
    main()
