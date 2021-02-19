import numpy as np
import random as rnd

from parts.Leaf import Leaf

class YearOneLeaf(Leaf):
    def __init__(self):
        self.pos = np.array([int(rnd.random() * 50),
                             int(rnd.random() * 50),
                             int(rnd.random() * 50)])
        self.reached = False
