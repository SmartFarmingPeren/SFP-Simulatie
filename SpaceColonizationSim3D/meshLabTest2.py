import os

import pymeshlab


def main():
    # DIR = os.getcwd() + '\\xyz/'
    # DIR = DIR.replace('\\', '/')
    # THICKMESHDIR = "/thick/"
    # DIR += THICKMESHDIR
    # files = os.listdir(DIR)
    ms = pymeshlab.MeshSet()

    # for file in files:
    print("loading mesh...")
    ms.load_new_mesh("C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/GeneratedTrees/mesh.ply")
    print("finished loading mesh...")
    print("get alpha complex shape")
    ms.alpha_complex_shape()
    print("finished alpha complex shape")
    ms.save_current_mesh("C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/GeneratedTrees/mesh2.ply")
    # ms.compute_normals_for_point_sets()
    # ms.compute_normals_for_point_sets()
    # ms.alpha_complex_shape()
    # ms.save_current_mesh("C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/GeneratedTrees/output")

    # ms = pymeshlab.MeshSet()


if __name__ == '__main__':
    main()
