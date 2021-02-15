import matplotlib.pyplot as plt
from Parts.tree import Tree
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

PointSize = 2 / 2


class PlotApp:
    def __init__(self, w_width=400, w_height=400):
        self.tree = Tree()
        self.generation = 0

        self.leaves_xarray = []
        self.leaves_yarray = []
        self.leaves_zarray = []
        self.splitLeaves()

        self.branches_xarray = []
        self.branches_yarray = []
        self.branches_zarray = []
        self.splitBranches()

        self.window_height = w_height
        self.window_width = w_width
        self.fig = plt.figure('3D Space Colonization Algorithm')
        self.ax = Axes3D(self.fig)

        self.ax.set_xlabel('Width')
        self.ax.set_xlim3d(0, 500)
        self.ax.set_ylabel('Height')
        self.ax.set_ylim3d(0, 500)
        self.ax.set_zlabel('Depth')
        self.ax.set_zlim3d(0, 500)

        # Generate buttons
        axReset = plt.axes([0.7, 0.02, 0.1, 0.075])
        self.bReset = Button(axReset, 'Reset')
        self.bReset.on_clicked(self.reset)

        axGrow = plt.axes([0.2, 0.02, 0.1, 0.075])
        self.bGrow = Button(axGrow, 'Grow')
        self.bGrow.on_clicked(self.grow_tree)

        # Set camera to front-facing.
        self.ax.view_init(elev=100, azim=90)

    def show(self):
        plt.show()

    def grow_tree(self, event):
        i = 0
        while i < 10:
            self.tree.grow()
            i += 1

        self.clear_canvas()
        self.update()

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
        self.update()

    def clearArrays(self):
        self.branches_xarray.clear()
        self.branches_yarray.clear()
        self.branches_zarray.clear()
        self.leaves_xarray.clear()
        self.leaves_yarray.clear()
        self.leaves_zarray.clear()

    def update(self):
        self.clearArrays()
        self.splitLeaves()
        self.splitBranches()
        self.draw()

    def draw(self):
        self.ax.scatter3D(self.leaves_xarray,
                          self.leaves_yarray,
                          self.leaves_zarray,
                          s=5,
                          c="green")

        Thiccness = 1
        for branch in self.tree.branches:
            if branch.parent is not None:
                x = [branch.pos[0][0], branch.parent.pos[0][0]]
                y = [branch.pos[1][0], branch.parent.pos[1][0]]
                z = [branch.pos[2][0], branch.parent.pos[2][0]]
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

    def splitLeaves(self):
        for leaf in self.tree.leaves:
            self.leaves_xarray.append(leaf.pos[0][0])
            self.leaves_yarray.append(leaf.pos[1][0])
            self.leaves_zarray.append(leaf.pos[2][0])

    def splitBranches(self):
        for branch in reversed(self.tree.branches):
            self.branches_xarray.append(branch.pos[0][0])
            self.branches_yarray.append(branch.pos[1][0])
            self.branches_zarray.append(branch.pos[2][0])

    def checkforTruncate(self, branch):
        count = 0
        for b in self.tree.branches:
            if all((b.pos - 5) < branch.pos) and all(branch.pos < (b.pos + 5)):
                count += 1
        if count > 1:
            return True
        else:
            return False
