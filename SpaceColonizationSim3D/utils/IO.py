import datetime
import os
import open3d as o3d

import RotationTest
from parts import Tree


# Save tree to seperate xyz files
def save_tree(tree: Tree):
    base, leaves, expanded = tree.save()
    save_part('base', base)
    save_part('expanded', expanded)
    save_part('leaves', leaves)


def save_part(part_name, points):
    path = 'xyz/' + part_name + '/'
    get_or_create_dir(path)

    amount_of_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

    location = path + 'gen_' + str(amount_of_files) + '_' + str(
        datetime.date.today().strftime("%d_%m")) + '_' + part_name + '.xyz'

    save_pcd_to_xyz(points, location)

    return location


def get_or_create_dir(path):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path))


def save_pcd_to_xyz(pcd: o3d.geometry.PointCloud, location):
    save_points_to_xyz(pcd.points, location)


def save_points_to_xyz(points, location):
    f = open(location, "a")
    for point in points:
        f.write("%f %f %f\n" % (point[0], point[1], point[2]))
    f.close()


# Load tree from seperate parts using the tree's ID
# For example id = 'gen_0_16_03'
def load_tree(id='gen_0_16_03'):
    base = load_part('base', id)
    expanded = load_part('expanded', id)
    leaves = load_part('leaves', id)
    return base, expanded, leaves


def load_part(part_name, id):
    path = 'xyz/' + part_name + '/' + id + '_' + part_name + '.xyz'
    if os.path.isfile(path):
        f = open(path, "r")
        points = []
        for line in f.readlines():
            points.append([float(e) for e in line.split(" ")])
        f.close()
        return points
    else:
        print("Cannot find part '%s' with id '%s' in '%s'!" % (part_name, id, path))


# View tree in open3d
def view():
    RotationTest.view_pointclouds([points_to_pcd(part) for part in load_tree()])


def points_to_pcd(points):
    pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
    return pcd

