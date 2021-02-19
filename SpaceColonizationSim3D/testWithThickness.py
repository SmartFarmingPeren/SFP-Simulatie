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
    for point in points:
        pointz = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2]) + '\n'
        f.write(pointz)
    f.close()