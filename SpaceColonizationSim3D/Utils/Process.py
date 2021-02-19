import matplotlib.pyplot as plt
import os
import os.path
import datetime
import math
from multiprocessing import Process
from parts.Tree import Tree
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button
pi = math.pi

def PointsInCircum(r, x, y, z, n=100):
    return [(math.cos(2*pi/n*I)*r+x, y, math.sin(2*pi/n*I)*r+z) for I in range(0,n+1)]

class treeProcess(Process):


    def __init__(self, ax):
        super(treeProcess, self).__init__()
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
                        if self.checkforTruncate(branch):
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

    def checkforTruncate(self, branch):
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
            circle = PointsInCircum(math.log(math.log(branch.Thickness) + 1) ** 2, branch.pos[0], branch.pos[1], branch.pos[2])
            for point in circle:
                branchesWithThiccness.append(point)
        with open(DIR + '/gen' + str(amount_of_files) + '_' + str(datetime.date.today().strftime("%d_%m")) +  "_centroid_thickness.xyz", 'w') as f:
            for branch in branchesWithThiccness:
                points = str(branch[0]) + ' ' + str(branch[1]) + ' ' + str(branch[2]) + '\n'
                f.write(points)
            f.close()