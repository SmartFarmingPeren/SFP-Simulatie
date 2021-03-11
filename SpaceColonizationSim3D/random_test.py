#!/usr/bin/python
import os

import numpy as np

n = 36000
r = 10
generateFixed = True
# save circle
DIR = os.getcwd() + '\\xyz/'
DIR = DIR.replace('\\', '/')
amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
origin = [51, 51, 51]

# Using readlines()
file1 = open(DIR + 'test_rotation.xyz', 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

if (generateFixed, origin):
    print("Generating fixed %d points on a sphere centered at the origin" % (n))
    points = []
    alpha = 4.0*np.pi*r*r/n
    d = np.sqrt(alpha)
    m_nu = int(np.round(np.pi/d))
    d_nu = np.pi/m_nu
    d_phi = alpha/d_nu
    count = 0
    for m in range (0,m_nu):
        nu = np.pi*(m+0.5)/m_nu
        m_phi = int(np.round(2*np.pi*np.sin(nu)/d_phi))
        for n in range (0,m_phi):
            phi = 2*np.pi*n/m_phi
            xp = r*np.sin(nu)*np.cos(phi)
            yp = r*np.sin(nu)*np.sin(phi)
            zp = r*np.cos(nu)
            points.append([xp + origin[0], yp+ origin[1], zp+ origin[2]])
            count = count +1

    with open(
            DIR + "test_rotation.xyz",
            'w') as f:
        for point in points:
            pointz = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2]) + '\n'
            f.write(pointz)
        f.close()