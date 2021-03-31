import open3d as o3d
import numpy as np

from utils import IO


class Viewer:
    def __init__(self):
        self.model = IO.points_to_pcd(IO.load_tree()[1])
        self.draw_key_callbacks()

    def draw_key_callbacks(self):
        model: o3d.geometry.PointCloud = self.model

        def rotate_y(vis: o3d.visualization.Visualizer):
            """
            Demo update function that rotated the pointcloud by 1 degree each time you press the mapped button is mapped to
            :param vis: input visualizer
            """
            vis.clear_geometries()
            model.rotate(o3d.geometry.get_rotation_matrix_from_xyz([0.0, np.deg2rad(1.0), 0.0]))
            vis.add_geometry(model)

        # map [spacebar] to the update() function
        callback = {ord(" "): rotate_y}
        o3d.visualization.draw_geometries_with_key_callbacks([self.model], key_to_callback=callback, width=1080,
                                                             height=720)
