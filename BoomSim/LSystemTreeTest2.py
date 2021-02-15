# variables: F + - [ ]
# axiom: F
# rules: (F -> FF+[+F-F-F]-[-F+F+F])

from Rules import Rule


def main():
    axiom = "F"

    Rule1 = Rule("F", "FF+[+F-F-F]-[-F+F+F]")
    Ruleset = [Rule1]

    depth = 5

    GenerateLSystem(axiom, Ruleset, depth)


def GenerateLSystem(ax, Rs, d):
    nextGen = ""

    i = 0
    for chars in ax:
        found = False
        for rule in Rs:
            if chars == rule.input:
                found = True
                nextGen += rule.output
        if not found:
            nextGen += chars

    print(nextGen)
    if d > 1:
        d -= 1
        GenerateLSystem(nextGen, Rs, d)



if __name__ == '__main__':
    main()
