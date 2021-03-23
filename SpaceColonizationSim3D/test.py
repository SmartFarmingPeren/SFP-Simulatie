import unittest
import numpy as np
import random as rnd
from utils.CONFIGFILE import POINTS_PER_SPHERE

from parts.Tree import calculate_distance, create_sphere

class Test_calculate_distance(unittest.TestCase):
    def test_calculate_distance(self):
        """
        Test if distance is within the right range
        """
        data = np.array([rnd.randint(0, 254),
                                     rnd.randint(0, 254),
                                     rnd.randint(0, 254)])
        data1 = np.array([rnd.randint(0, 254),
                                     rnd.randint(0, 254),
                                     rnd.randint(0, 254)])

        result = calculate_distance(data, data1)
        self.assertTrue((result > 0))

        result1 = calculate_distance(data1, data)
        self.assertTrue((result > 0))

        self.assertTrue((result == result1)) # distance from a to b as to be the same as from b to a

class Test_create_sphere(unittest.TestCase):
    """
    Test is the spheres are created correctly
    """
    def test_create_sphere(self):
        data = rnd.uniform(1, 3.0) # thickness
        # point from where to generate
        data1 = np.array([rnd.randint(0, 254),
                                     rnd.randint(0, 254),
                                     rnd.randint(0, 254)])
        i = 0
        j = 0
        
        result = create_sphere(data, data1)
        
        while i < POINTS_PER_SPHERE:
            while j < 3:
                self.assertTrue(((result[i][j] > 0) and (result[i][j] > 0) and (result[i][j] > 0)))
                j += 1
            j = 0`
            i += 1
        


if __name__ == '__main__':
    unittest.main()