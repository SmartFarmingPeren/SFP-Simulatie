import os
import os.path
import datetime
import math
from multiprocessing import Process

import numpy as np

import RotationTest
from parts.Tree import Tree
pi = math.pi


# https://stackoverflow.com/questions/8487893/generate-all-the-points-on-the-circumference-of-a-circle
def points_in_circum(r, origin, direction, n=100):
    x, y, z = origin
    points = [((math.cos(2*pi/n*I)*r+x), y, math.sin(2*pi/n*I)*r+z) for I in range(0,n+1)]
    rotated_points = []
    for point in points:
        rotated_points.append(RotationTest.rotate_around_point(point, origin, direction))
    return rotated_points

# Roteerd een punt om een ander punt heen.
# Moet nog werken met proporties, als een richting (1, 0, .5) is houd het niet rekening mee dat z kleiner is dan x.
def rotate_around_point(input, origin, direction):
    x_axis, y_axis, z_axis = calculate_axes(direction)

    #This is from: https://en.wikipedia.org/wiki/Rotation_matrix
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

    #Removing origin(middle point) from the input(point of the circle) to remove unwanted behevior
    translated_input = [input[0] - origin[0], input[1] - origin[1], input[2] - origin[2]]

    output = np.matmul(r_total, translated_input)

    return output + origin

#calculate the different axis
#probably something wrong with this.
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

class TreeProcess(Process):

    def __init__(self, ax):
        super(TreeProcess, self).__init__()
        self.tree = Tree()
        self.generation = 0
        self.ax = ax
        self.thick_tree = []

    def run(self):
        self.grow_tree()
        self.thick_tree = self.add_thickness()
        self.save()

    def grow_tree(self):
        i = 0
        while i < 20:
            self.tree.grow()
            i += 1

    def add_thickness(self):
        branches_with_thiccness = []
        for branch in self.tree.branches:
            circle = points_in_circum(math.sqrt(branch.Thickness/10 + 1), branch.pos, branch.direction)
            for point in circle:
                branches_with_thiccness.append(point)
        return branches_with_thiccness

    #Save pointcloid to xyz format
    def save(self):
        DIR = os.getcwd() + '\\xyz'
        DIR = DIR.replace('\\', '/')
        amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        # save barebone version of tree without _THICCNESS_
        with open(DIR + '/gen' + str(amount_of_files) + '_' + str(datetime.date.today().strftime("%d_%m")) +  "_centroid.xyz", 'w') as f:
            for branch in self.tree.branches:
                points = str(branch.pos[0]) + ' ' + str(branch.pos[1]) + ' ' + str(branch.pos[2]) + '\n'
                f.write(points)
            f.close()
        # save _THICCNESS_ version of tree
        with open(DIR + '/gen' + str(amount_of_files) + '_' + str(datetime.date.today().strftime("%d_%m")) +  "_centroid_thickness.xyz", 'w') as f:
            for branch in self.thick_tree:
                points = str(branch[0]) + ' ' + str(branch[1]) + ' ' + str(branch[2]) + '\n'
                f.write(points)
            f.close()
