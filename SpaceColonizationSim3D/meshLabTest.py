import os

import pymeshlab


def main():
    MESHLABDIR = ""
    APLHADIR = ""
    BUFFEREDNORMALSDIR = ""
    INPUTMESHESDIR = ""

    ms = pymeshlab.MeshSet()

    # for file in files:
    print("loading mesh...")
    ms.load_new_mesh("C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/xyz/gen29_10_03_centroid_thickness.xyz")
    print("finished loading mesh...")
    ms.set_current_mesh(0)
    print("compute normals")
    ms.compute_normals_for_point_sets()
    print("finished computing")
    ms.save_current_mesh("C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/GeneratedTrees/mesh.ply")
    # print("get alpha complex shape")
    # ms.alpha_complex_shape()
    # print("finished alpha complex shape")
    # ms.compute_normals_for_point_sets()
    # ms.compute_normals_for_point_sets()
    # ms.alpha_complex_shape()
    # ms.save_current_mesh("C:/Users/lucav/Documents/GitHub/SFP-Simulatie/SpaceColonizationSim3D/GeneratedTrees/output")

    # ms = pymeshlab.MeshSet()


if __name__ == '__main__':
    main()
