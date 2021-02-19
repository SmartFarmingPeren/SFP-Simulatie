import os
import os.path
import datetime
import math
from multiprocessing import Process

import numpy as np

from parts.Tree import Tree
pi = math.pi


# https://stackoverflow.com/questions/8487893/generate-all-the-points-on-the-circumference-of-a-circle
def points_in_circum(r, origin, direction, n=100):
    x, y, z = origin
    print(x,y,z)
    points = [((math.cos(2*pi/n*I)*r+x), y, math.sin(2*pi/n*I)*r+z) for I in range(0,n+1)]
    rotated_points = []
    for point in points:
        rotated_points.append(rotate_around_point(point, origin, direction))
    return rotated_points

def rotate_around_point(input, origin, direction):
    x_axis, y_axis, z_axis = (0, 0, 0)

    if direction[0] != 0:
        if direction[1] == 0:
            x_axis = np.tan(direction[1] / np.sqrt(direction[0] ** 2 + direction[1] ** 2))
        else:
            x_axis = np.deg2rad(90)
    else:
        x_axis = 0

    if direction[0] != 0:
        if direction[2] != 0:
            y_axis = np.tan(direction[2] / np.sqrt(direction[0] ** 2 + direction[2] ** 2))
        else:
            y_axis = np.deg2rad(90)
    else:
        y_axis = 0

    if direction[2] != 0:
        if direction[1] == 0:
            z_axis = np.tan(direction[1] / np.sqrt(direction[2] ** 2 + direction[1] ** 2))
        else:
            z_axis = np.deg2rad(90)
    else:
        z_axis = 0

    pitch = x_axis
    yaw = y_axis
    roll = z_axis

    x_rotation = [[np.cos(yaw), -np.sin(yaw), 0],
                  [np.sin(yaw), np.cos(yaw), 0],
                  [0, 0, 1]]
    y_rotation = [[np.cos(pitch), 0, np.sin(pitch)],
                  [0, 1, 0],
                  [-np.sin(pitch), 0, np.cos(pitch)]]
    z_rotation = [[1, 0, 0],
                  [0, np.cos(roll), -np.sin(roll)],
                  [0, np.sin(roll), np.cos(roll)]]
    r_total = np.matmul(np.matmul(x_rotation, y_rotation), z_rotation)

    translated_input = input - origin
    output = np.matmul(r_total, translated_input)
    return output + origin

class TreeProcess(Process):

    def __init__(self, ax):
        super(TreeProcess, self).__init__()
        self.tree = Tree()
        self.generation = 0
        self.ax = ax

    def run(self):
        self.grow_tree()
        self.save()

    def grow_tree(self):
        i = 0
        while i < 100:
            self.tree.grow()
            i += 1

        self.clear_canvas()

    def clear_canvas(self):
        self.ax.cla()
        self.ax.set_xlabel('Width')
        self.ax.set_xlim3d(0, 500)
        self.ax.set_ylabel('Height')
        self.ax.set_ylim3d(0, 500)
        self.ax.set_zlabel('Depth')
        self.ax.set_zlim3d(0, 500)
        self.ax.view_init(elev=100, azim=90)

    def reset(self, event):
        self.clear_canvas()
        self.tree.reshuffleLeaves()
        self.tree.newTree()
        #self.update()

    #def update(self):
        #self.draw()

    def draw(self):
        leavesPosX = []
        leavesPosY = []
        leavesPosZ = []
        for leaf in self.tree.leaves:
            leavesPosX.append(leaf.pos[0])
            leavesPosY.append(leaf.pos[1])
            leavesPosZ.append(leaf.pos[2])
        self.ax.scatter3D(leavesPosX,
                          leavesPosY,
                          leavesPosZ,
                          s=5,
                          c="green")

        Thiccness = 1
        for branch in self.tree.branches:
            if branch.parent is not None:
                x = [branch.pos[0], branch.parent.pos[0]]
                y = [branch.pos[1], branch.parent.pos[1]]
                z = [branch.pos[2], branch.parent.pos[2]]
                if Thiccness >= 1:
                    if not branch.last:
                        if self.check_for_truncate(branch):
                            branch.color = "red"
                    self.ax.plot3D(x,
                                   y,
                                   z,
                                   c=branch.color,
                                   linewidth=Thiccness)
                    # Thiccness *= 0.995
        # self.ax.plot3D(self.branches_xarray,
        #                self.branches_yarray,
        #                self.branches_zarray,
        #                c="blue")

    def check_for_truncate(self, branch):
        count = 0
        for b in self.tree.branches:
            if all((b.pos - 5) < branch.pos) and all(branch.pos < (b.pos + 5)):
                count += 1
        if count > 1:
            return True
        else:
            return False

    def save(self):
        DIR = os.getcwd() + '\\SpaceColonizationSim3D\\xyz'
        DIR = DIR.replace('\\', '/')
        amount_of_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
#        for branch in reversed(self.tree.branches):
 #           branch.length = 2
  #          if(branch.parent is not None):
   #             dirx = branch.parent.pos[0] - branch.pos[0]
    #            print(dirx)
     #           diry = branch.parent.pos[1] - branch.pos[1]
      #          print(diry)
       #         dirz = branch.parent.pos[2] - branch.pos[2]
        #        print(dirz)
         #       direct = [dirx, diry, dirz]
          #      print(direct)
           #     print(branch.direction)
            #    branch.direction = direct
             #   print(branch.direction)
              #  i = 0
               # print('length : ' + str(branch.length) + " || direction : " + str(branch.direction[0]) + ':' + str(branch.direction[1]) + ':' + str(branch.direction[2]))
                #while i < 5:
                 #   i += 1
                  #  self.tree.branches.append(branch.next())
                   # branch.length += 2 
        with open(DIR + '/gen' + str(amount_of_files) + '_' + str(datetime.date.today().strftime("%d_%m")) +  "_centroid.xyz", 'w') as f:
            for branch in self.tree.branches:
                points = str(branch.pos[0]) + ' ' + str(branch.pos[1]) + ' ' + str(branch.pos[2]) + '\n'
                f.write(points)
            f.close()
        branchesWithThiccness = []
        for branch in self.tree.branches:
            circle = points_in_circum(math.sqrt(branch.Thickness/10 + 1), branch.pos, branch.direction)
            for point in circle:
                branchesWithThiccness.append(point)
        with open(DIR + '/gen' + str(amount_of_files) + '_' + str(datetime.date.today().strftime("%d_%m")) +  "_centroid_thickness.xyz", 'w') as f:
            for branch in branchesWithThiccness:
                points = str(branch[0]) + ' ' + str(branch[1]) + ' ' + str(branch[2]) + '\n'
                f.write(points)
            f.close()