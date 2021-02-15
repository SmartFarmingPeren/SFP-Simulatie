from tkinter import *
import math

length = 120
angle = math.pi/4
depth = 1
max_depth = 7

class Main:
    def __init__(self):
        self.window_height = 600
        self.window_width = 600
        self.starting_x = int(self.window_width / 2)
        self.starting_y = self.window_height
        self.starting_angle = 0
        window = Tk()
        window.title("Recursive tree generator")

        self.canvas = Canvas(window, width=self.window_width, height=self.window_height, bg="gray")
        self.canvas.pack()

        self.branch(depth, length, angle, self.starting_x, self.starting_y, self.starting_x, self.starting_y - 100)

        mainloop()

    def branch(self,depth, length, a, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)
        x2_old = x2
        y2_old = y2
        x2, y2 = self.AngleTransposition(a , length, x2, y2)
        x1 = x2_old
        y1 = y2_old
        a += 45/(2*depth)


        if length > 10:
            depth += 1
            self.branch(depth,length * 0.67, a, x1, y1, x2, y2)
            self.branch(depth,length * 0.67, -a, x1, y1, x2, y2)



    # https://stackoverflow.com/questions/29989792/rotate-line-in-tkinter-canvas
    # Kevin: May 1, 2015
    def AngleTransposition(self, angle, leng, starting_x, starting_y):
        length = leng
        ang = angle
        point_x = starting_x
        point_y = starting_y

        end_x = point_x + (length * math.sin(ang))
        end_y = point_y - (length * math.cos(ang))

        return end_x, end_y

Main()
