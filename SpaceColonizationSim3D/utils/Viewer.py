import open3d as o3d


class Viewer:
    def __init__(self, tree):
        self.tree = tree
        self.models = []
        self.draw_key_callbacks()

    def draw_key_callbacks(self):
        tree = self.tree
        models = self.models

        def update(vis):
            models.clear()
            tree.grow()
            pc = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(tree.branches[0].get_points_to_save([])))
            pc.paint_uniform_color((.1, .8, .1))
            models.append(pc)

        callback = {ord(" "): update}
        o3d.visualization.draw_geometries_with_key_callbacks(self.models, key_to_callback=callback, width=1080,
                                                             height=720)
