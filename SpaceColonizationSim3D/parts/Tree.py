import random
from typing import List

import numpy as np
import open3d as o3d
from utils import IO

from parts.Branch import Branch, get_next
from parts.Leaf import Leaf
from parts.Section import Section
from utils.CONFIGFILE import AMOUNT_OF_LEAVES, POINTS_PER_SPHERE, MIN_DIST, MAX_DIST, SPHERE_RADIUS_DIVISOR, \
    CENTER_DEVIATION, CENTER_X, CENTER_Z, CENTER_Y


# Made by minor 20/21 without comments so understanding is a bit difficult.
# Comments that are there are from 21/21 from our understanding of the code.
def calculate_distance(pos_begin, pos_destination):
    """
    This function calculates the distance between the closest leaf and the known branch.
    :param pos_begin: This is the coordinate of the branch that is already known.
    :param pos_destination: This is the coordinate of the closest leaf.
    :return: This is an integer always > 0 that tells the distance from pos_begin to pos_destination
    """
    absolute_x_y_z = np.absolute(pos_begin - pos_destination)
    distance = int(absolute_x_y_z[0] ** 2 + absolute_x_y_z[1] ** 2 + absolute_x_y_z[2] ** 2)

    return distance


def create_sphere(radius, origin):
    """
    This function is used to generate the spheres that form the tree
    np.math.sqrt(section.thickness / 10 + 1), section.pos
    :param radius: This is the sqrt from the thickness of that specific point, used to make the sphere the right size
    for the position it is used in.
    :param origin: Origin is the center of the sphere where the points will be generated around
    :return: The function returns all the point that make the sphere
    """
    if SPHERE_RADIUS_DIVISOR != 0:
        radius /= SPHERE_RADIUS_DIVISOR
    resolution = radius * POINTS_PER_SPHERE
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


class Tree:
    def __init__(self):
        self.leaves: List[Leaf] = []
        self.thick = []
        self.root = None
        self.new_tree()

    # inits a new tree
    def new_tree(self):
        """
        This function is used to create a new tree first the root of the tree is determined
        Next a scan to the closest leaf is done, generating the root branch and the first split of branches
        """
        # TODO add method to remove all branches (resursively)
        # self.branches.clear()

        self.add_leaves()

        # pos = np.array([50, 0.0, 37.5])
        if CENTER_DEVIATION > 0:
            x_low = CENTER_X - CENTER_DEVIATION
            x_high = CENTER_X + CENTER_DEVIATION
            z_low = CENTER_Z - CENTER_DEVIATION
            z_high = CENTER_Z + CENTER_DEVIATION
            pos = np.array([random.randint(x_low, x_high), CENTER_Y, random.randint(z_low, z_high)])
        else:
            pos = np.array([CENTER_X, CENTER_Y, CENTER_Z])
        # pos = np.array([random.randint(40, 60), 0.0, random.randint(30, 45)])
        direction = np.array([0.0, 1.0, 0.0])
        self.root = Branch(age=1)
        self.root.sections.append(Section(pos, direction, None))

        found = False
        while not found:
            for leaf in self.leaves:
                distance = calculate_distance(leaf.pos, self.root.get_last_pos())
                # Euclidean distance is normally calculated by the square root of all elements summed and multiplied
                # to the power of 2 (Dist). Multiplying the Min_ and Max_distance beforehand to the power of 2,
                # removes the need for a square root, thus speeding up the program.
                if MAX_DIST > distance > MIN_DIST:
                    found = True

            if not found:
                self.root.add_section()

    def grow(self):
        """
        Looks from all the leaves if a branch is in range, the closest leaf to a branch will make the branch extend
        towards that leaf
        """
        for leaf in reversed(self.leaves):
            reached = False
            distance_table = []
            for branch in get_next(self.root):
                for section in branch.sections:
                    distance = calculate_distance(leaf.pos, section.pos)
                    distance_table.append([section, distance])

            closest_section, shortest_distance = min(distance_table, key=lambda t: t[1])
            # if closest section is outside the distance range
            if not (MIN_DIST < shortest_distance< MAX_DIST):
                if shortest_distance < MIN_DIST:
                    reached = True
            else:
                # sets the direction for the next section in the growable branch
                new_dir = leaf.pos - closest_section.pos
                factor = np.linalg.norm(new_dir)
                new_dir = new_dir / factor
                closest_section.direction = closest_section.direction + new_dir
                closest_section.count += 1

            if reached:
                self.leaves.remove(leaf)

        # Go through every branch, create a new branch for every growable section that isnt the last section.
        # Otherwise just create a new section in the same branch
        for branch in get_next(self.root):
            for section in branch.sections:
                if section.count > 0:
                    section.direction = section.direction / section.count
                    if section.pos is not branch.get_last_pos():
                        branch.next(section.next())
                    else:
                        branch.add_section()
                section.reset()

    def add_leaves(self):
        """
        add AMOUNT_OF_LEAVES leaves to the tree to start generation
        :return list of new leaves
        """
        for _ in range(AMOUNT_OF_LEAVES):
            self.leaves.append(Leaf())
        return self.leaves

    def save(self):
        """
        save all the point in a point cloud
        """
        
        return [self.to_pcd(), self.leaves_to_pcd(), IO.points_to_pcd(self.thick)]

    def to_pcd(self):
        """
        Puts all the points of the leaves, spheres etc in a point cloud and returns this point cloud to the function that
        called it
        """
        points = self.get_all_points()
        colors = []
        for branch in get_next(self.root):
            for _ in branch.sections:
                colors.append(branch.return_color())
        pcd = IO.points_to_pcd(points)
        pcd.colors = o3d.utility.Vector3dVector(np.asarray(colors))
        return pcd

    def leaves_to_pcd(self):
        """
        This function is used to save the leaves in a xyz file
        """
        return IO.points_to_pcd(list(self.save_leaves()))

    def save_leaves(self):
        """
        This function is used to save all leaves
        """
        for leaf in self.leaves:
            yield leaf.pos

    def get_all_points(self):
        """
        This function is used to gather all the points that are used in branches
        """
        for branch in get_next(self.root):
            for section in branch.sections:
                yield section.pos

    def add_thickness(self):
        """
        This function is used to generate the spheres on the right place, making sure young branches are thinner
        and older branches less thin
        """
        branches_with_thickness = []
        for branch in get_next(self.root):
            for section in branch.sections:
                # circle = points_in_circum(math.sqrt(branch.thickness / 10 + 1), branch.pos, branch.direction)
                circle = create_sphere(np.math.sqrt(section.thickness / 10 + 1), section.pos)
                for point in circle:
                    branches_with_thickness.append(point)
        return branches_with_thickness

    # https://www.journaldev.com/23022/height-of-a-tree-data-structure#height-of-the-tree-8211-iteratively
    def refresh_age(self, branch: Branch):
        """
        NOT USED AT THE MOMENT
        """
        if branch is None:
            return 0
        heights = []
        for child in branch.children:
            height = self.refresh_age(child)
            heights.append(height)
        height = max(heights) + 1 if len(heights) > 0 else 1
        branch.age = height
        return height