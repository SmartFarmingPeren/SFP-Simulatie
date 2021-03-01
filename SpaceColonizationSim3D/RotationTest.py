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

#Creates a circle around a point
def points_in_circum(r, origin, n=100):
    x, y, z = origin
    points = [[(np.cos(2 * np.pi / n * I) * r + x), y, np.sin(2 * np.pi / n * I) * r + z] for I in range(0, n + 1)]

    return points


# Roteerd een punt om een ander punt heen.
# Moet nog werken met proporties, als een richting (1, 0, .5) is houd het niet rekening mee dat z kleiner is dan x.
def rotate_around_point(input, origin, direction):
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

    roll = x_axis
    yaw = y_axis
    pitch = z_axis

    #This is from: https://en.wikipedia.org/wiki/Rotation_matrix
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

    #Removing origin(middle point) from the input(point of the circle) to remove unwanted behevior
    translated_input = [input[0] - origin[0], input[1] - origin[1], input[2] - origin[2]]

    output = np.matmul(r_total, translated_input)

    return output + origin


# werkt maar z coördinaten worden niet veranderd.
def rotateZ3D(theta, input):
    sinTheta = np.sin(np.deg2rad(theta))
    cosTheta = np.cos(np.deg2rad(theta))
    output = input
    output[0] = input[0] * cosTheta - input[1] * sinTheta
    output[1] = input[1] * cosTheta - input[0] * sinTheta
    return output


# werkt maar z coördinaten worden niet veranderd.
def rotateX3D(theta, input):
    sinTheta = np.sin(np.deg2rad(theta))
    cosTheta = np.cos(np.deg2rad(theta))
    output = input
    output[0] = input[1] * cosTheta - input[2] * sinTheta
    output[1] = input[2] * cosTheta - input[1] * sinTheta
    return output


# werkt maar z coördinaten worden niet veranderd.
def rotateY3D(theta, input):
    sinTheta = np.sin(np.deg2rad(theta))
    cosTheta = np.cos(np.deg2rad(theta))
    output = input
    output[0] = input[0] * cosTheta - input[2] * sinTheta
    output[1] = input[2] * cosTheta - input[0] * sinTheta
    return output


def main():
    origin = [0, 0, 0]
    points = points_in_circum(40, origin)
    rotated_points = []
    for point in points:
        # rotated_points.append(rotate_around_point(point, origin, [1, 0, 0]))
        rotated_points.append(rotateZ3D(90, point))

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
