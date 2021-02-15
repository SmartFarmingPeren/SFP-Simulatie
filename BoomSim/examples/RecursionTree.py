from tkinter import *
import math
import random

start_angle = 25
start_length = 30
max_rand = 40


# noinspection SpellCheckingInspection
class TreeCanvas:
    def __init__(self, LSystem, rs):
        self.LSystem = LSystem
        self.Ruleset = rs

        self.window_height = 700
        self.window_width = 700

        self.window = Tk()
        self.window.title("Recursive tree generator")

        self.sliderLengthWidget = Scale(self.window, label="Length", length=200, from_=1, to=200, resolution=1,
                                        sliderlength=20, orient=HORIZONTAL)
        self.sliderLengthWidget.set(start_length)
        self.sliderLengthWidget.grid(row=0, column=0)
        # self.sliderLengthWidget.pack(side="bottom")

        self.sliderAngleWidget = Scale(self.window, label="Angle", length=200, from_=0, to=90, resolution=0.5,
                                       sliderlength=20, orient=HORIZONTAL)
        self.sliderAngleWidget.set(start_angle)
        self.sliderAngleWidget.grid(row=1, column=0)
        # self.sliderAngleWidget.pack(side="bottom")

        self.sliderDepthWidget = Scale(self.window, label="Recursive Layers", length=200, from_=0, to=10, resolution=1,
                                       sliderlength=20, orient=HORIZONTAL)
        self.sliderDepthWidget.set(5)
        self.sliderDepthWidget.grid(row=2, column=0)
        # self.sliderAngleWidget.pack(side="bottom")

        Button(self.window, text='Update', command=self.show_values).grid(row=3, column=0)
        Button(self.window, text='Reset', command=self.clear).grid(row=4, column=0)

        self.canvas = Canvas(self.window, width=self.window_width, height=self.window_height, bg="gray")
        self.canvas.grid(row=0, column=1, rowspan=5)
        # self.canvas.pack()

    def clear(self):
        self.canvas.delete("all")
        self.sliderDepthWidget.set(0)
        self.sliderLengthWidget.set(start_length)
        self.sliderAngleWidget.set(start_angle)
        self.LSystem.axiom = self.LSystem.Ruleset[0].input

    def show_values(self):
        a = 0
        # a = start_angle
        lengte = self.sliderLengthWidget.get()
        diepte = self.sliderDepthWidget.get()
        self.LSystem.axiom = self.LSystem.GenerateLSystem(self.LSystem.axiom, self.Ruleset, 0)
        self.turtle(self.LSystem.axiom, self.window_width / 3, self.window_height, lengte, a)

        self.sliderDepthWidget.set(diepte - 1)
        self.sliderLengthWidget.set(lengte * 0.67)
        self.sliderAngleWidget.set(self.sliderAngleWidget.get() * 1)

    def turtle(self, sentence, x1, y1, length, angle):
        color = 'white'
        X_Stack = []
        Y_Stack = []
        Angle_Stack = []
        a = self.sliderAngleWidget.get()

        random.seed(random.randint(1, 10))

        for char in sentence:
            current = char
            if current == "F":
                x2, y2 = self.X_Y_AngleTranslation(length, angle, x1, y1)
                self.canvas.create_line(x1, y1, x2, y2, fill=color)
                x1 = x2
                y1 = y2
            elif current == "+":
                angle += a
            elif current == "-":
                angle -= a
            elif current == "[":
                X_Stack.append(x1)
                Y_Stack.append(y1)
                Angle_Stack.append(angle)
            elif current == "]":
                x1 = X_Stack.pop()
                y1 = Y_Stack.pop()
                angle = Angle_Stack.pop()

    def X_Y_AngleTranslation(self, length, angle, start_x, start_y):
        leng = length
        ang = angle
        point_x = start_x
        point_y = start_y

        end_x = point_x + (leng * math.sin(math.radians(ang)))
        end_y = point_y - (leng * math.cos(math.radians(ang)))

        return end_x, end_y

    def ColorSelector(self, diepte):
        switcher = {
            0: "red",
            1: "green",
            2: "cyan",
            3: "magenta",
            4: "yellow"
        }
        return switcher.get(diepte,"white")