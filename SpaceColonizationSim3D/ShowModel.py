import open3d as o3d
import os

# show circle
DIR = os.getcwd() + '\\xyz/'
DIR = DIR.replace('\\', '/')
model = o3d.io.read_point_cloud("C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/GeneratedTrees/" + "mesh2.ply")
print(model)
o3d.visualization.draw_geometries([model], width=1080, height=720)
