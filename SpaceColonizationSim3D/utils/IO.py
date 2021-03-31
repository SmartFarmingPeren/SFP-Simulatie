import datetime
import os

import open3d as o3d

from parts import Tree


def save_tree(tree: Tree):
    """
    Used to save the different parts of the tree to xyz files. Namely the base, expanded(real tree) and leaves
    """
    base, leaves, expanded = tree.save()
    save_part('base', base)
    save_part('expanded', expanded)
    save_part('leaves', leaves)


def save_part(part_name, points):
    """
    Used to generate the file location path
    :rtype: Returns the location of the folder the file is placed in
    """
    path = 'xyz/' + part_name + '/'
    get_or_create_dir(path)

    amount_of_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

    location = path + 'gen_' + str(amount_of_files) + '_' + str(
        datetime.date.today().strftime("%d_%m")) + '_' + part_name + '.xyz'

    save_pcd_to_xyz(points, location)

    return location


def get_or_create_dir(path):
    """
    Used to find the existing directories or creates new directories for the xyz files
    """
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path))


def save_pcd_to_xyz(pcd: o3d.geometry.PointCloud, location):
    """
    Used to save the point cloud to a xyz file
    """
    save_points_to_xyz(pcd.points, location)


def save_points_to_xyz(points, location):
    """
    Used to save the point from the point cloud into the xzy file
    """
    f = open(location, "a")
    for point in points:
        f.write("%f %f %f\n" % (point[0], point[1], point[2]))
    f.close()


def load_tree(id='gen_20_25_03'):
    """
    Load tree from separate parts using the tree's ID, for example id = 'gen_0_16_03'
    :rtype: Returns the base, expanded and leaves of the tree
    """
    base = load_part('base', id)
    expanded = load_part('expanded', id)
    leaves = load_part('leaves', id)
    return base, expanded, leaves


def load_part(part_name, id):
    """
    Used to load a specific part of the tree
    :rtype: Returns the points used to form the tree
    """
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


def view(id='gen_20_25_03'):
    """
    View parts of a tree in open3d
    """
    view_pointclouds([points_to_pcd(part) for part in load_tree(id)])


def points_to_pcd(points):
    """
    Form a point cloud from the generated points
    :rtype: Returns the generated point cloud
    """
    pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
    return pcd


def view_pointclouds(pcds):
    """
    Makes it possible to view the point cloud using open3d
    """
    o3d.visualization.draw_geometries(pcds, width=1080, height=720, mesh_show_back_face=False)


def view_models(model_names):
    """
    Makes it possible to view pointcloud files by reading them as open3d.PointCloud object
    """
    models = []
    for name in model_names:
        models.append(o3d.io.read_point_cloud(name))
    o3d.visualization.draw_geometries(models, width=1080, height=720, mesh_show_back_face=False)
