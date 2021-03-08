from typing import List

import numpy as np
from parts.Leaf import Leaf
from parts.Branch import Branch
from parts.Section import Section
from parts.yearOne.YearOneLeaf import YearOneLeaf
from utils import TreeProcess
from utils.Viewer import Viewer

AMOUNT_OF_LEAVES: int = 200
MIN_DIST: int = 400  # 20 ** 2, minimal distance is squared to remove a slow square root
MAX_DIST: int = 2500  # 50 ** 2, maximal distance is squared to remove a slow square root


# Made by minor 20/21 without comments so understanding is a bit difficult.
# Comments that are there are from 21/21 from our understanding of the code.
def calculate_distance(pos_begin, pos_destination):
    absolute_x_y_z = np.absolute(pos_begin - pos_destination)
    distance = int(absolute_x_y_z[0] ** 2 + absolute_x_y_z[1] ** 2 + absolute_x_y_z[2] ** 2)
    return distance


class Tree:
    def __init__(self):
        self.leaves: List[Leaf] = []
        self.branches: List[Branch] = []
        self.reshuffle_leaves()
        self.root = None
        self.new_tree()
        # self.viewer = Viewer(self)

    # inits a new tree
    def new_tree(self):
        # TODO add method to remove all branches (resursively)
        # self.branches.clear()

        pos = np.array([250.0, 0.0, 250.0])
        direction = np.array([0.0, 5.0, 0.0])
        self.root = Branch()
        self.root.sections.append(Section(pos, direction, None))
        self.branches.append(self.root)

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

            for section in self.root.sections:
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

        # go through every branch, create a new branch for every growable section that isnt the last section , otherwise just create a new section in the same branch
        for branch in reversed(self.branches):
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
        points = self.root.get_points_to_save([])
        print(points)
        return points

    def save_leaves(self):
        for leaf in self.leaves:
            yield leaf.pos

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
