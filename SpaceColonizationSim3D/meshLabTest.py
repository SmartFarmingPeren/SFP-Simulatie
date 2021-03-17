import os
from time import sleep

import pymeshlab


def convert_xyz_to_ply(BUFFERDIR, DIR, THICKMESHDIR, ms):
    thick_mesh_files = os.listdir(DIR + THICKMESHDIR)
    index = 0
    for thick_mesh in thick_mesh_files:
        print(thick_mesh)
        ms.load_new_mesh(DIR + THICKMESHDIR + thick_mesh)
        ms.set_current_mesh(index)
        thick_mesh = thick_mesh.split(".")[0]
        ms.save_current_mesh(DIR + BUFFERDIR + thick_mesh + ".ply")
        index += 1


def generate_alpha_complex_shapes(ALPHASHAPEDIR, BUFFERDIR, DIR, ms):
    thick_mesh_ply_files = os.listdir(DIR + BUFFERDIR)
    index = 0
    for thick_mesh_ply in thick_mesh_ply_files:
        print(thick_mesh_ply)
        ms.load_new_mesh(DIR + BUFFERDIR + thick_mesh_ply)
        ms.set_current_mesh(index)
        ms.alpha_complex_shape()
        thick_mesh_ply = thick_mesh_ply.split(".")[0]
        ms.save_current_mesh(DIR + ALPHASHAPEDIR + thick_mesh_ply + ".ply")
        index += 1


def main():
    DIR = os.getcwd() + '\\meshLab/'
    DIR = DIR.replace('\\', '/')
    THICKMESHDIR = "input_meshes/"
    BUFFERDIR = "buffer_ply/"
    ALPHASHAPEDIR = "alpha_complex_shapes_output/"
    ms = pymeshlab.MeshSet()

    convert_xyz_to_ply(BUFFERDIR, DIR, THICKMESHDIR, ms)
    ms.clear()
    generate_alpha_complex_shapes(ALPHASHAPEDIR, BUFFERDIR, DIR, ms)


if __name__ == '__main__':
    main()
