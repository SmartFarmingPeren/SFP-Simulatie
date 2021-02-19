import datetime
import math
import os
pi = math.pi

def PointsInCircum(r,n=100):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r, 250) for x in range(0,n+1)]

branch = [250, 500, 250]
thickness = 40
points = []

points = PointsInCircum(thickness)


DIR = os.getcwd() + '\\SpaceColonizationSim3D\\xyz'
DIR = DIR.replace('\\', '/')
amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
with open(DIR + '/gen' + str(amount_of_files) + '_' + str(datetime.date.today().strftime("%d_%m")) +  "_centroid.xyz", 'w') as f:
    for point in points:
        pointz = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2]) + '\n'
        f.write(pointz)
    f.close()