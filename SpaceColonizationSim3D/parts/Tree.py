import numpy as np
import math
from parts.Leaf import Leaf
from parts.Branch import Branch
from parts.yearOne.YearOneLeaf import YearOneLeaf

amount_of_leaves = 200
min_dist = 400  # 20 ** 2, minimal distance is squared to remove a slow square root
max_dist = 2500  # 50 ** 2, maximal distance is squared to remove a slow square root


# Made by minor 20/21 without comments so understanding is a bit difficult.
# Comments that are there are from 21/21 from our understanding of the code.
def calculate_distance(pos_begin, pos_destination):
    absolute_x_y_z = np.absolute(pos_begin - pos_destination)
    distance = int(absolute_x_y_z[0] ** 2 + absolute_x_y_z[1] ** 2 + absolute_x_y_z[2] ** 2)
    return distance


class Tree:
    def __init__(self):
        self.leaves = []
        self.reshuffle_leaves()

        self.branches = []
        self.root = None
        self.new_tree()

    def grow(self):
        i = 0
        print(len(self.branches))  # just here to let you know that it is running and how big the tree is.
        # calculates the distance any branch has to any leaf(points to grow to) and calculates the absolute shortest
        # of all branches and grow to that leaf for each leaf.
        for leaf in self.leaves:
            j = 0
            closest_branch = None
            closest_record = 1000
            for branch in self.branches:
                distance = calculate_distance(leaf.pos, branch.pos)
                if distance < min_dist:
                    leaf.reached = True
                    closest_branch = None
                    break
                elif closest_branch is None or distance < closest_record:
                    closest_branch = branch
                    closest_record = distance
                elif distance > max_dist:
                    pass
                j += 1
            i += 1

            # Adds the direction the branch should travel to to the existing direction
            if closest_branch is not None:
                new_direction = leaf.pos - closest_branch.pos
                factor = np.linalg.norm(new_direction)
                new_direction = new_direction / factor
                closest_branch.direction = closest_branch.direction + new_direction
                closest_branch.count += 1

        # removes any leaves that are 'reached'
        for leaf in reversed(self.leaves):
            if leaf.reached:
                self.leaves.remove(leaf)

        # if a branch was at least the closest to one leaf, grow that branch.
        for branch in reversed(self.branches):
            if branch.count > 0:
                branch.direction = branch.direction / branch.count
                self.branches.append(branch.next())
            branch.reset()

    def reshuffle_leaves(self):
        self.leaves.clear()
        for _ in range(amount_of_leaves):
            self.leaves.append(Leaf())

    # not yet implemented, first year leaves are meant to be the 4 guiding branches
    def reshuffle_first_year_leaves(self):
        self.leaves.clear()
        for _ in range(amount_of_leaves):
            self.leaves.append(YearOneLeaf())

    # inits a new tree
    def new_tree(self):
        self.branches.clear()

        pos = np.array([250,
                        0,
                        250])
        direction = np.array([0,
                              5,
                              0])
        self.root = Branch(pos, direction, True)
        self.branches.append(self.root)

        current = self.root

        found = False
        while not found:
            for leaf in self.leaves:
                distance = calculate_distance(current.pos, leaf.pos)
                # Euclidean distance is normally calculated by the square root of all elements summed and multiplied
                # to the power of 2 (Dist). Multiplying the Min_ and Max_distance beforehand to the power of 2,
                # removes the need for a square root, thus speeding up the program.
                if max_dist > distance > min_dist:
                    found = True

            if not found:
                branch = current.next()
                current = branch
                self.branches.append(current)

    def trim_leaves(self):
        for leaf in reversed(self.leaves):
            if 225 < leaf.pos[0] < 275:
                self.leaves.remove(leaf)
            elif 225 < leaf.pos[2] < 275:
                self.leaves.remove(leaf)
