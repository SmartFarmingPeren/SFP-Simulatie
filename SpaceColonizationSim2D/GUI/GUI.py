import math
from tkinter import *
from Parts.tree import Tree

PointSize = int(4 / 2)


class TreeCanvas:
    def __init__(self, w_width=400, w_height=400, start_angle=25, start_length=30, start_depth=0):
        self.window_height = w_height
        self.window_width = w_width

        self.tree = Tree()
        self.start_angle = start_angle
        self.start_length = start_length
        self.start_depth = start_depth

        self.window = Tk()
        self.window.title("Space Colonization Algorithm")

        Button(self.window, text='Grow', command=self.grow_tree).grid(row=3, column=0)
        Button(self.window, text='Update', command=self.update).grid(row=4, column=0)
        Button(self.window, text='Reset', command=self.clear).grid(row=5, column=0)

        self.canvas = Canvas(self.window, width=self.window_width, height=self.window_height, bg="gray")
        self.canvas.grid(row=0, column=1, rowspan=6)

    def grow_tree(self):
        i = 0
        while i < 40:
            self.tree.grow()
            self.canvas.update()
            self.canvas.delete("leaves")
            self.draw()
            i += 1

    def clear(self):
        self.canvas.delete("all")
        self.tree.reshuffleLeaves()
        self.tree.newTree()
        self.update()

    def update(self):
        self.draw()

    def draw(self):
        for leaf in self.tree.leaves:
            self.canvas.create_oval(leaf.pos[0][0] - PointSize, leaf.pos[1][0] - PointSize,
                                    leaf.pos[0][0] + PointSize, leaf.pos[1][0] + PointSize,
                                    fill="white",
                                    tags="leaves")
        for branch in self.tree.branches:
            if branch.parent is not None:
                if branch.last:
                    branch.color = "green"
                elif self.checkforTruncate(branch):
                    branch.color = "red"
                else:
                    branch.color = "white"
                self.canvas.create_line(branch.parent.pos[0][0], branch.parent.pos[1][0],
                                        branch.pos[0][0], branch.pos[1][0],
                                        fill=branch.color,
                                        tags="branches",
                                        width=1.5)

    def X_Y_AngleTranslation(self, length, angle, start_x, start_y):
        leng = length
        ang = angle
        point_x = start_x
        point_y = start_y

        end_x = point_x + (leng * math.sin(math.radians(ang)))
        end_y = point_y - (leng * math.cos(math.radians(ang)))

        return end_x, end_y

    def checkforTruncate(self, branch):
        count = 0
        for b in self.tree.branches:
            if all((b.pos - 5) < branch.pos) and all(branch.pos < (b.pos + 10)):
                count += 1

        if count > 1:
            return True
        else: return False
