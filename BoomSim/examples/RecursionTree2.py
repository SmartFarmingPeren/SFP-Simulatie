from tkinter import *
import math

a = 30
l = 100


# noinspection SpellCheckingInspection
class TreeCanvas:
    def __init__(self):
        self.window_height = 700
        self.window_width = 700

        self.window = Tk()
        self.window.title("Recursive tree generator")

        self.sliderLengthWidget = Scale(self.window, label="Length", length=200, from_=10, to=200, resolution=5,
                                        sliderlength=20, orient=HORIZONTAL)
        self.sliderLengthWidget.set(l)
        self.sliderLengthWidget.grid(row=0, column=0)
        # self.sliderLengthWidget.pack(side="bottom")

        self.sliderAngleWidget = Scale(self.window, label="Angle", length=200, from_=0, to=90, resolution=5,
                                       sliderlength=20, orient=HORIZONTAL)
        self.sliderAngleWidget.set(a)
        self.sliderAngleWidget.grid(row=1, column=0)
        # self.sliderAngleWidget.pack(side="bottom")

        self.sliderDepthWidget = Scale(self.window, label="Recursive Layers", length=200, from_=0, to=15, resolution=1,
                                       sliderlength=20, orient=HORIZONTAL)
        self.sliderDepthWidget.set(1)
        self.sliderDepthWidget.grid(row=2, column=0)
        # self.sliderAngleWidget.pack(side="bottom")

        Button(self.window, text='Update', command=self.show_values).grid(row=3, column=0)

        self.canvas = Canvas(self.window, width=self.window_width, height=self.window_height, bg="gray")
        self.canvas.grid(row=0, column=1, rowspan=5)
        # self.canvas.pack()

        mainloop()

    def show_values(self):
        self.canvas.delete("all")
        hoek = self.sliderAngleWidget.get()
        lengte = self.sliderLengthWidget.get()
        diepte = self.sliderDepthWidget.get()
        self.branch(lengte, hoek, self.window_width / 2, self.window_height, self.window_width / 2,
                    self.window_height - lengte, diepte)
        self.branch(lengte, -hoek, self.window_width / 2, self.window_height, self.window_width / 2,
                    self.window_height - lengte, diepte)

    def branch(self, length, angle, x1, y1, x2, y2, diepte):
        self.canvas.create_line(x1, y1, x2, y2, fill="white")
        x1 = x2
        y1 = y2
        x2, y2 = self.X_Y_AngleTranslation(length, angle, x2, y2)
        diepte -= 1
        if diepte > 0 and length > 1:
            self.branch(length * 0.67, angle + a, x1, y1, x2, y2, diepte)
            self.branch(length * 0.67, angle - a, x1, y1, x2, y2, diepte)
        else:
            self.blossom(x1, y1, x2, y2)

    def blossom(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1-2, y1-3, x1+2, y1+5, fill="magenta")

    def AngleModifier(self, angle):
        if angle < 0:
            return angle - a
        elif angle >= 0:
            return angle + a

    def X_Y_AngleTranslation(self, length, angle, start_x, start_y):
        leng = length
        ang = angle
        point_x = start_x
        point_y = start_y

        end_x = point_x + (leng * math.sin(math.radians(ang)))
        end_y = point_y - (leng * math.cos(math.radians(ang)))

        return end_x, end_y

