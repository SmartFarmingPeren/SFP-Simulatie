# import tkinter as tk
# from tkinter import HORIZONTAL
#
# from ProcessManager import ProcessManager
# from utils.CONFIGFILE import AMOUNT_OF_TREES
#
# text_fields = ['Sort of tree',  # DDL of trees, e.g. V Hague, standard, T shaped
#                'Add thickness value',
#                # Thickness added to the tree thickess each iteration (value between 0.1 and 1 (or 2))
#                'Amount of leaves',
#                # Leaves are points to which tree branches will grow, not a leaf (more leaves == more branches)
#                'Sphere density',  # The density of the generated sphere (360 - 1080)
#                'Tree size',  # The amount of growth iterations the tree will do (100 - 300)
#                'Amount of trees']  # The amount of trees that will be generated consecutively
#
#
# def save_values(entries):
#     for entry in entries:
#         field = entry[0]
#         text = entry[1].get()
#         print('%s: "%s"' % (field, text))
#
#
# def start_generation():
#     manager = ProcessManager(AMOUNT_OF_TREES)
#     manager.grow_tree()
#
#
# def makeform(root, fields):
#     entries = []
#     for field in fields:
#         row = tk.Frame(root)
#         lab = tk.Label(row, width=25, text=field, anchor='w')
#         ent = tk.Entry(row)
#         row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
#         lab.pack(side=tk.LEFT)
#         ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
#         entries.append((field, ent))
#     return entries
#
#
# def main():
#     root = tk.Tk()
#
#     ents = makeform(root, text_fields)
#     root.bind('<Return>', (lambda event, e=ents: save_values(e)))
#     b1 = tk.Button(root, text='Save values',
#                    command=(lambda e=ents: save_values(e)))
#     b1.pack(side=tk.LEFT, padx=5, pady=5)
#     b2 = tk.Button(root, text='Generate tree', command=(lambda e=ents: start_generation()))
#     b2.pack(side=tk.LEFT, padx=5, pady=5)
#     b2 = tk.Button(root, text='Quit', command=root.quit)
#     b2.pack(side=tk.LEFT, padx=5, pady=5)
#
#     w = tk.Scale(root, from_=0, to=200, orient=HORIZONTAL)
#     w.pack()
#
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()

import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Standard_tree_page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)


class V_hague_tree_page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        tk.Label(self, text="This is page 2").pack()

        tk.Label(self, text="This is page 2").pack(side="left")
        w = tk.Scale(self, from_=0, to=200, orient=tk.HORIZONTAL)
        w.pack(side="right")
        label.pack(side="top", fill="both", expand=True)


class Main_view(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        standard_tree_page = Standard_tree_page(self)
        v_hague_tree_page = V_hague_tree_page(self)

        button_frame = tk.Frame(self)
        container = tk.Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        standard_tree_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        v_hague_tree_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(button_frame, text="Standard tree", command=standard_tree_page.lift)
        b2 = tk.Button(button_frame, text="V-hague", command=v_hague_tree_page.lift)

        b1.pack(side="left")
        b2.pack(side="left")

        standard_tree_page.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = Main_view(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x600")
    root.mainloop()
