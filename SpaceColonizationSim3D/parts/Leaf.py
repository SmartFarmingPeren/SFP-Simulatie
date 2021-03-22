import numpy as np
import random as rnd
from datetime import datetime

from utils.CONFIGFILE import GENERATE_V_HAGUE


class Leaf:
    def __init__(self, pos=None):
        self.pos = np.array([0, 0, 0])

        if pos is None:
            if GENERATE_V_HAGUE:
                if rnd.randint(0, 1):
                    self.pos = np.array([rnd.randint(0, 40),
                                         rnd.randint(50, 100),
                                         rnd.randint(0, 75)])
                else:
                    self.pos = np.array([rnd.randint(60, 100),
                                         rnd.randint(30, 100),
                                         rnd.randint(0, 75)])
            else:
                self.pos = np.array([rnd.randint(50, 449),
                                     rnd.randint(100, 499),
                                     rnd.randint(50, 449)])
        else:
            self.pos = pos
        self.reached = False

# self.pos = np.array([rnd.randint(50, 449),
#                      rnd.randint(200, 499),
#                      rnd.randint(50, 339)])

# self.pos = np.array([int(rnd.random() * 400) + 50,
#                      int(500 - rnd.random() * 300),
#                      int(rnd.random() * 400) + 50])