from typing import List

import numpy as np
import open3d as o3d
from parts.Leaf import Leaf
from parts.Branch import Branch, get_next
from parts.Section import Section
from parts.yearOne.YearOneLeaf import YearOneLeaf
from utils import IO

AMOUNT_OF_LEAVES: int = 200
MIN_DIST: int = 400  # 20 ** 2, minimal distance is squared to remove a slow square root
MAX_DIST: int = 2500  # 50 ** 2, maximal distance is squared to remove a slow square root


# Made by minor 20/21 without comments so understanding is a bit difficult.
# Comments that are there are from 21/21 from our understanding of the code.
def calculate_distance(pos_begin, pos_destination):
    absolute_x_y_z = np.absolute(pos_begin - pos_destination)
    distance = int(absolute_x_y_z[0] ** 2 + absolute_x_y_z[1] ** 2 + absolute_x_y_z[2] ** 2)
    return distance


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


class Tree:
    def __init__(self):
        self.leaves: List[Leaf] = []
        self.thick = []
        self.reshuffle_leaves()
        self.root = None
        self.new_tree()
        # self.viewer = Viewer(self)

    # inits a new tree
    def new_tree(self):
        # TODO add method to remove all branches (resursively)
        # self.branches.clear()

        pos = np.array([250.0, 0.0, 250.0])
        direction = np.array([0.0, 1.0, 0.0])
        self.root = Branch(level=1, color=np.array([0.3, 1.0, 0.6]))
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
            print(found)

    def grow(self):
        for leaf in self.leaves:
            closest_section = None
            closest_record = 1000

            for branch in get_next(self.root):
                for section in branch.sections:
                    distance = calculate_distance(leaf.pos, section.pos)
                    # if a section reached a leaf, break
                    if distance < MIN_DIST:
                        leaf.reached = True
                        closest_section = None
                        break
                    # elif distance is smaller compared to thsee previously closest ction, make this the closest
                    elif closest_section is None or distance < closest_record:
                        closest_section = section
                        closest_record = distance
                    # filter out points that are too far away from the point (kinda pointless)
                    elif distance > MAX_DIST:
                        pass

            # sets the direction for the next section in the growable branch
            if closest_section is not None:
                new_dir = leaf.pos - closest_section.pos
                factor = np.linalg.norm(new_dir)
                new_dir = new_dir / factor
                closest_section.direction = closest_section.direction + new_dir
                closest_section.count += 1

        # removes any leaves that are 'reached'
        for leaf in reversed(self.leaves):
            if leaf.reached:
                self.leaves.remove(leaf)

        # TODO add recursive search through branches using yield?
        # go through every branch, create a new branch for every growable section that isnt the last section , otherwise just create a new section in the same branch
        for branch in get_next(self.root):
            for section in branch.sections:
                if section.count > 0:
                    section.direction = section.direction / section.count
                    if section.pos is not branch.get_last_pos():
                        branch.next(section.next())
                    else:
                        branch.add_section()
                section.reset()
        # if a branch was at least the closest to one leaf, grow that branch.
        # self.root.grow()

    def reshuffle_leaves(self):
        self.leaves.clear()
        for _ in range(AMOUNT_OF_LEAVES):
            self.leaves.append(Leaf())

    # not yet implemented, first year leaves are meant to be the 4 guiding branches
    def reshuffle_first_year_leaves(self):
        self.leaves.clear()
        for _ in range(AMOUNT_OF_LEAVES):
            self.leaves.append(YearOneLeaf())

    def trim_leaves(self):
        for leaf in reversed(self.leaves):
            if 225 < leaf.pos[0] < 275:
                self.leaves.remove(leaf)
            elif 225 < leaf.pos[2] < 275:
                self.leaves.remove(leaf)

    def save(self):
        return [self.to_pcd(), self.leaves_to_pcd(), IO.points_to_pcd(self.thick)]

    # method
    def to_pcd(self):
        points = self.get_all_points()
        colors = []
        for branch in get_next(self.root):
            for _ in branch.sections:
                colors.append(branch.color)
        pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
        pcd.colors = o3d.utility.Vector3dVector(np.asarray(colors))
        return pcd

    def save_leaves(self):
        for leaf in self.leaves:
            yield leaf.pos

    def leaves_to_pcd(self):
        points = list(self.save_leaves())
        pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
        return pcd

    def get_all_points(self):
        for branch in get_next(self.root):
            for section in branch.sections:
                yield section.pos

    def add_thickness(self):
        branches_with_thickness = []
        for branch in get_next(self.root):
            for section in branch.sections:
                # circle = points_in_circum(math.sqrt(branch.thickness / 10 + 1), branch.pos, branch.direction)
                circle = create_sphere(np.math.sqrt(section.thickness / 10 + 1), section.pos)
                for point in circle:
                    branches_with_thickness.append(point)
        return branches_with_thickness

    # def subdivide(self):
    #     print("SUBDIVIDING POINTS")
    #     count = 0
    #     for branch in self.branches:
    #         branch.subdivide()
    #         count += len(branch.sections)
    #     print("NEW SIZE: %d" % count)

    # def add_thickness(self):
    #     for branch in self.branches:
    #         branch.add_thickness()
    #
    # def add_thickness_circles(self):
    #     branches_with_thickness = []
    #     for branch in self.branches:
    #         for section in branch.sections:
    #             circle = TreeProcess.points_in_circum(np.math.sqrt(section.thickness / 10 + 1), section.pos, section.direction)
    #             for point in circle:
    #                 branches_with_thickness.append(point)
    #     return branches_with_thickness
