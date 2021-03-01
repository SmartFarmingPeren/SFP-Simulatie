import numpy as np
import random as rnd


class Leaf:
    def __init__(self, pos=None):
        self.pos = np.array([0, 0, 0])
        if pos is None:
            self.pos = np.array([int(rnd.random() * 400)+50,
                                 int(500 - rnd.random() * 300),
                                 int(rnd.random() * 400)+50])
        else:
            self.pos = pos
        self.reached = False
