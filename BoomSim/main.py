from Rules import Rule
from LSystemTreeTest1 import Lsystem
from examples.RecursionTree import TreeCanvas


# variables: F + - [ ]
# axiom: F
# rules: (F -> FF+[+F-F-F]-[-F+F+F])

# variables: AB
# axiom: A
# rules: (A->AB),(B->A)

# variables: F X + - [ ]
# axiom: X
# rule1: F --> FF
# rule2: X --> F-[[X]+X]+F[+FX]-X
# angle: 22.5


def main():
    tree1 = Lsystem("XXXXXF", [Rule("F", "FF-[-F+F+F-F+]+[+F-F-F-F+]")], 0)
    tree2 = Lsystem("X", [Rule("X", "F-[[X]+X]+F[+FX]-X"), Rule("F", "FF")], 0)
    tree3 = Lsystem("F", [Rule("F", "FF+[+F-F-F]-[-F+F+F]")],0)
    # sentence = tree.GenerateLSystem(tree.axiom, tree.Ruleset,5)
    canvas = TreeCanvas(tree2, tree2.Ruleset)
    # canvas.turtle(sentence, tree.Ruleset, canvas.window_width / 2,
    #               canvas.window_height, l, a)

    print("done")
    canvas.window.mainloop()


if __name__ == '__main__':
    main()
