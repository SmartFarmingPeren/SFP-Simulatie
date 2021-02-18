import numpy as np
import random as rnd


class Leaf:
    def __init__(self):
        self.pos = np.array([[150 + int(rnd.random() * 200)], #wind manipulatie
                             [150 + int(rnd.random() * 200)],
                              [250 + int(rnd.random() * 200)]]) #wind manipulatie
        self.reached = False
