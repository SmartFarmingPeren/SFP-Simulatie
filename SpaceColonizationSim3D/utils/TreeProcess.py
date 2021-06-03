import math
from multiprocessing import Process

from utils import IO

from parts.Tree import Tree
from utils.CONFIGFILE import TREE_SIZE

PI = math.pi


class TreeProcess(Process):
    """
    This class is used to generate trees
    """
    def __init__(self):
        super(TreeProcess, self).__init__()
        self.tree = Tree()

        # self.grow_tree()
        # self.tree.refresh_age(self.tree.root)
        # self.tree.thick = self.tree.add_thickness()
        # IO.save_tree(self.tree)

    def run(self):
        """
        Main function that runs in order to generate the trees
        """
        self.grow_tree()
        self.tree.refresh_age(self.tree.root)
        self.tree.thick = self.tree.add_thickness()
        IO.save_tree(self.tree)
        pass

    def grow_tree(self):
        """
        Used to actually grow the tree
        """
        # change tree_size to your preference. ideal size is between 100 and 150
        tree_size = TREE_SIZE
        for i in range(tree_size):
            print("%3.2f%% complete.." % (i * 100 / tree_size))
            self.tree.grow()