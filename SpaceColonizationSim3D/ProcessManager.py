import os
import os.path
import datetime
from utils.Process import TreeProcess
from parts.Tree import Tree

PointSize = 2 / 2


class Manager():
    def __init__(self, w_width=800, w_height=800):
        self.tree = Tree()
        self.generation = 0

    def grow_tree(self, event):
        i = 0
        while i < 1:
            tmp = TreeProcess(self.ax)
            tmp.start()
            i += 1
