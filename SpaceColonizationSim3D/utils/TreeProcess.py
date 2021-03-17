import math
from multiprocessing import Process
from parts.Tree import Tree
from utils import IO

PI = math.pi


# # https://stackoverflow.com/questions/8487893/generate-all-the-points-on-the-circumference-of-a-circle
# def points_in_circum(r, origin, direction, n=100):
#     x, y, z = origin
#     points = [((math.cos(2 * PI / n * I) * r + x), y, math.sin(2 * PI / n * I) * r + z) for I in range(0, n + 1)]
#     rotated_points = []
#     for point in points:
#         rotated_points.append(RotationTest.rotate_around_point(point, origin, direction))
#     return rotated_points
#
#
# # Rotate a point(input) around another point(origin).
# # Does not yet work with propositions,
# # given a direction (1, 0, 0.5) for example the code should give a z_rotation of less than 90 but this is not the case.
# def rotate_around_point(input, origin, direction, x, y, z):
#     x_axis, y_axis, z_axis = calculate_axes(direction)
#
#     # This is from: https://en.wikipedia.org/wiki/Rotation_matrix
#     x_rotation = [[1, 0, 0],
#                   [0, np.cos(z_axis), -np.sin(z_axis)],
#                   [0, np.sin(z_axis), np.cos(z_axis)]]
#     y_rotation = [[np.cos(y_axis), 0, np.sin(y_axis)],
#                   [0, 1, 0],
#                   [-np.sin(y_axis), 0, np.cos(y_axis)]]
#     z_rotation = [[np.cos(x_axis), -np.sin(x_axis), 0],
#                   [np.sin(x_axis), np.cos(x_axis), 0],
#                   [0, 0, 1]]
#     r_total = np.matmul(np.matmul(x_rotation, z_rotation), y_rotation)
#
#     # Removing origin(middle point) from the input(point of the circle) to remove unwanted behevior
#     translated_input = [input[0] - origin[0], input[1] - origin[1], input[2] - origin[2]]
#
#     output = np.matmul(r_total, translated_input)
#
#     return output + origin


class TreeProcess(Process):

    def __init__(self):
        super(TreeProcess, self).__init__()
        self.tree = Tree()

        self.grow_tree()
        self.tree.thick = self.tree.add_thickness()
        IO.save_tree(self.tree)

    def run(self):
        # self.grow_tree()
        # self.tree.thick = self.tree.add_thickness()
        # self.save()
        pass

    def grow_tree(self):
        # change tree_size to your preference. ideal size is between 100 and 150
        tree_size = 150
        for i in range(tree_size):
            print("%3.2f%% complete.." % (i * 100 / tree_size))
            self.tree.grow()