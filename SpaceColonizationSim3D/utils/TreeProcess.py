import os
import os.path
import datetime
import math
from multiprocessing import Process

import numpy as np

import RotationTest
from parts.Tree import Tree

PI = math.pi


# https://stackoverflow.com/questions/8487893/generate-all-the-points-on-the-circumference-of-a-circle
def points_in_circum(r, origin, direction, n=100):
    x, y, z = origin
    points = [((math.cos(2 * PI / n * I) * r + x), y, math.sin(2 * PI / n * I) * r + z) for I in range(0, n + 1)]
    rotated_points = []
    for point in points:
        rotated_points.append(RotationTest.rotate_around_point(point, origin, direction))
    return rotated_points


# Rotate a point(input) around another point(origin).
# Does not yet work with propositions,
# given a direction (1, 0, 0.5) for example the code should give a z_rotation of less than 90 but this is not the case.
def rotate_around_point(input, origin, direction, x, y, z):
    x_axis, y_axis, z_axis = calculate_axes(direction)

    # This is from: https://en.wikipedia.org/wiki/Rotation_matrix
    x_rotation = [[1, 0, 0],
                  [0, np.cos(z_axis), -np.sin(z_axis)],
                  [0, np.sin(z_axis), np.cos(z_axis)]]
    y_rotation = [[np.cos(y_axis), 0, np.sin(y_axis)],
                  [0, 1, 0],
                  [-np.sin(y_axis), 0, np.cos(y_axis)]]
    z_rotation = [[np.cos(x_axis), -np.sin(x_axis), 0],
                  [np.sin(x_axis), np.cos(x_axis), 0],
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

def create_sphere(radius, origin):
    resolution = radius * 1500
    points = []
    alpha = 4.0 * np.pi * radius * radius / resolution
    d = np.sqrt(alpha)
    m_nu = int(np.round(np.pi / d))
    d_nu = np.pi / m_nu
    d_phi = alpha / d_nu
    count = 0
    for m in range(0, m_nu):
        nu = np.pi * (m + 0.5) / m_nu
        m_phi = int(np.round(2 * np.pi * np.sin(nu) / d_phi))
        for resolution in range(0, m_phi):
            phi = 2 * np.pi * resolution / m_phi
            xp = radius * np.sin(nu) * np.cos(phi)
            yp = radius * np.sin(nu) * np.sin(phi)
            zp = radius * np.cos(nu)
            points.append([xp + origin[0], yp + origin[1], zp + origin[2]])
            count += 1
    return points


class TreeProcess(Process):

    def __init__(self):
        super(TreeProcess, self).__init__()
        self.tree = Tree()
        self.thick_tree = []
        self.grow_tree()
        # self.tree.subdivide()
        # self.tree.add_thickness_circles()
        self.save()

    def run(self):
        pass
        # self.grow_tree()
        # # self.thick_tree = self.add_thickness()
        # self.save()

    def grow_tree(self):
        # change tree_size to your preference. ideal size is between 100 and 150
        tree_size = 150
        for i in range(tree_size):
            print("%3.2f%% complete.." % (i * 100 / 150))
            self.tree.grow()

    def add_thickness(self):
        branches_with_thickness = []
        for branch in self.tree.branches:
            # circle = points_in_circum(math.sqrt(branch.thickness / 10 + 1), branch.pos, branch.direction)
            circle = create_sphere(math.sqrt(branch.thickness / 10 + 1), branch.pos)
            for point in circle:
                branches_with_thickness.append(point)
        return branches_with_thickness

    # Save point cloud to xyz format
    def save(self):
        # DIR = os.getcwd() + '\\xyz'
        # DIR = DIR.replace('\\', '/')
        # amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        # # save bare bone version of tree without _THICKNESS_
        # name = DIR + '/gen' + str(amount_of_files + 1) + '_' + str(
        #     datetime.date.today().strftime("%d_%m")) + "_centroid.xyz"
        # self.save_points_to_xyz(self.tree.save(), name)
        #
        # # save _THICKNESS_ version of tree
        # thick_name = DIR + '/gen' + str(amount_of_files) + '_' + str(
        #     datetime.date.today().strftime("%d_%m")) + "_centroid_thickness.xyz"
        # self.save_points_to_xyz(self.thick_tree, thick_name)

        RotationTest.view_pointclouds(self.tree.save())

    def save_leaves(self):
        DIR = os.getcwd() + '\\xyz'
        DIR = DIR.replace('\\', '/')
        amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        # save bare bone version of tree without _THICKNESS_
        location = DIR + '/leaves_' + str(datetime.date.today().strftime("%d_%m")) + ".xyz"
        self.save_points_to_xyz(self.tree.save_leaves(), location)

        return location

    @staticmethod
    def save_points_to_xyz(points, location):
        f = open(location, "a")
        for point in points:
            f.write("%f %f %f\n" % (point[0], point[1], point[2]))
        f.close()
