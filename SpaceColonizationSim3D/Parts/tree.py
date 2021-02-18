import numpy as np
import math
from Parts.leaf import Leaf
from Parts.branch import Branch

AmountOfLeaves = 200
min_dist = 400      # 20 ** 2, minimal distance is squared to remove a slow squareroot
max_dist = 2500      # 50 ** 2, maximal distance is squared to remove a slow squareroot


class Tree:
    def __init__(self):

        self.leaves = []  #array of object leaves
        self.reshuffleLeaves()  # makes new instances of leaves

        self.branches = []  #array of object branches
        self.root = None
        self.newTree()  #make a new tree

    def grow(self):
        i = 0


        for leaf in self.leaves:
            j = 0
            closestBranch = None
            closest_record = 1000
            for branch in self.branches:
                distance = self.calculateDistance(leaf.pos, branch.pos)
                print(branch.branchid)
                if distance < min_dist:
                    leaf.reached = True
                    closestBranch = None
                    break
                elif closestBranch is None or distance < closest_record:
                    closestBranch = branch
                    closest_record = distance
                elif distance > max_dist:
                    pass
                j += 1
            i += 1

            if closestBranch is not None:
                newDirection = leaf.pos - closestBranch.pos
                factor = np.linalg.norm(newDirection)
                newDirection = newDirection / factor
                closestBranch.direction = closestBranch.direction + newDirection
                closestBranch.count += 1

        for leaf in reversed(self.leaves):
            if leaf.reached:
                self.leaves.remove(leaf)

        for branch in reversed(self.branches):
            if branch.count > 0:
                branch.direction = branch.direction / branch.count
                self.branches.append(branch.next())
            branch.reset()

    def printLeaves(self):
        i = 0
        for leaf in self.leaves:
            print("Leaf " + str(i) + " x = " + str(leaf.pos[0]) +
                  " , y = " + str(leaf.pos[1]))
            i += 1

    def reshuffleLeaves(self):
        self.leaves.clear()  # remove all leaves
        i = 0
        while i < AmountOfLeaves:
            self.leaves.append(Leaf())
            # self.trimleaves()
            i += 1

    def newTree(self):
        self.branches.clear()

        pos = np.array([[250],
                        [500],
                        [250]])
        direction = np.array([[0],
                              [-5],
                              [0]])
        self.root = Branch(pos, direction, True)
        self.branches.append(self.root)

        current = self.root

        found = False
        while not found:
            for leaf in self.leaves:
                Dist = self.calculateDistance(current.pos, leaf.pos)
                # Euclidean distance is normally calculated by the squareroot of all elements summed and multiplied
                # to the power of 2 (Dist).
                # Multiplying the Min_ and Max_distance beforehand to the power of 2, removes the need for a squareroot,
                # thus speeding up the program.
                if max_dist > Dist > min_dist:
                    found = True

            if not found:
                branch = current.next()
                current = branch
                self.branches.append(current)

    def calculateDistance(self, posBegin, posDestination):
        Absolute_x_y_z = np.absolute(posBegin - posDestination)
        Distance = int(Absolute_x_y_z[0][0] ** 2 + Absolute_x_y_z[1][0] ** 2 + Absolute_x_y_z[2][0] ** 2)
        return Distance

    def trimleaves(self):
        for leaf in reversed(self.leaves):
            if  225 < leaf.pos[0][0] < 275:
                self.leaves.remove(leaf)
            elif 225 < leaf.pos[2][0]< 275:
                self.leaves.remove(leaf)