import random as rnd

import numpy as np

from utils.CONFIGFILE import KIND_OF_TREE, NORMAL_X_LOW, NORMAL_Z_HIGH, NORMAL_Z_LOW, NORMAL_Y_HIGH, NORMAL_X_HIGH, \
    NORMAL_Y_LOW, V_HAGUE_X_1_LOW, V_HAGUE_X_1_HIGH, V_HAGUE_Y_1_HIGH, V_HAGUE_Y_1_LOW, V_HAGUE_Z_1_HIGH, \
    V_HAGUE_Z_1_LOW, V_HAGUE_X_2_HIGH, V_HAGUE_X_2_LOW, V_HAGUE_Y_2_LOW, V_HAGUE_Y_2_HIGH, V_HAGUE_Z_2_HIGH, \
    V_HAGUE_Z_2_LOW


class Leaf:
    def __init__(self, pos=None):
        self.pos = np.array([0, 0, 0])

        if pos is None:
            if KIND_OF_TREE == 0:  # NORMAL TREE
                self.pos = np.array([rnd.randint(NORMAL_X_LOW, NORMAL_X_HIGH),
                                     rnd.randint(NORMAL_Y_LOW, NORMAL_Y_HIGH),
                                     rnd.randint(NORMAL_Z_LOW, NORMAL_Z_HIGH)])
            elif KIND_OF_TREE == 1:  # V-HAGUE
                if rnd.randint(0, 1):  # Generate points half the time at one side and half the time at the other side
                    self.pos = np.array([rnd.randint(V_HAGUE_X_1_LOW, V_HAGUE_X_1_HIGH),
                                         rnd.randint(V_HAGUE_Y_1_LOW, V_HAGUE_Y_1_HIGH),
                                         rnd.randint(V_HAGUE_Z_1_LOW, V_HAGUE_Z_1_HIGH)])
                else:
                    self.pos = np.array([rnd.randint(V_HAGUE_X_2_LOW, V_HAGUE_X_2_HIGH),
                                         rnd.randint(V_HAGUE_Y_2_LOW, V_HAGUE_Y_2_HIGH),
                                         rnd.randint(V_HAGUE_Z_2_LOW, V_HAGUE_Z_2_HIGH)])
        else:
            self.pos = pos
        self.reached = False

# self.pos = np.array([rnd.randint(50, 449),
#                      rnd.randint(200, 499),
#                      rnd.randint(50, 339)])

# self.pos = np.array([int(rnd.random() * 400) + 50,
#                      int(500 - rnd.random() * 300),
#                      int(rnd.random() * 400) + 50])
