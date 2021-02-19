import numpy as np
import random as rnd


class Leaf:
    def __init__(self):
        self.pos = np.array([[int(rnd.random() * 400)+50], #wind manipulatie
                             [int(rnd.random() * 300)],
                             [int(rnd.random() * 400)+50]]) #wind manipulatie
        self.reached = False
