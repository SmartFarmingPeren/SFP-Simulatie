import numpy as np
import math
import random as rnd
from Parts.leaf import Leaf
from Parts.branch import Branch

AmountOfLeaves = 400
min_dist = 100  # 10**2
max_dist = 400  # 20**2


class Tree:
    def __init__(self):
        self.leaves = []
        self.reshuffleLeaves()

        self.coords = []
        self.convertLeavestoCoords()
        self.branches = []
        self.root = None
        self.newTree()

    def grow(self):
        i = 0
        for leaf in self.leaves:
            j = 0
            closestBranch = None
            closest_record = 1000
            for branch in self.branches:
                distance = self.calculateDistance(leaf.pos, branch.pos)
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
        self.leaves.clear()
        i = 0
        while i < AmountOfLeaves:
            self.leaves.append(Leaf())
            i += 1
        # self.trimLeaves()

    def newTree(self):
        self.branches.clear()

        pos = np.array([[200],
                        [400]])
        direction = np.array([[0],
                              [-5]])
        self.root = Branch(pos, direction, True, "white")
        self.branches.append(self.root)

        current = self.root

        found = False
        while not found:
            for leaf in self.leaves:
                Dist = self.calculateDistance(current.pos, leaf.pos)
                if max_dist > Dist > min_dist:
                    found = True

            if not found:
                branch = current.next()
                current = branch
                self.branches.append(current)

    def calculateDistance(self, posBegin, posDestination):
        Absolute_x_y = np.absolute(posBegin - posDestination)
        Distance = int(Absolute_x_y[0][0] ** 2 + Absolute_x_y[1][0] ** 2)
        return Distance

    def trimLeaves(self):
        for leaf in reversed(self.leaves):
            x_value = leaf.pos[0][0]
            y_value = leaf.pos[1][0]
            if y_value > x_value:
                self.leaves.remove(leaf)
            elif x_value > 200:
                if y_value + x_value > 400:
                    self.leaves.remove(leaf)

    def convertLeavestoCoords(self):
        i = 0
        for leaf in self.leaves:
            self.coords.append([
                [int(rnd.random() * 300) + 50],
                [int(rnd.random() * 200) + 50],
                [int(rnd.random() * 50)]
            ])
            i += 1
