from Rules import Rule


class Lsystem:
    def __init__(self, axiom, Rs, depth):
        self.axiom = axiom
        self.Ruleset = Rs
        self.depth = depth

    def GenerateLSystem(self, ax, Rs, depth):
        nextGen = ""

        for chars in ax:
            found = False
            for rule in Rs:
                if chars == rule.input:
                    found = True
                    nextGen += rule.output
            if not found:
                nextGen += chars

        if depth > 1:
            depth -= 1
            return self.GenerateLSystem(nextGen, Rs, depth)
        else:
            return nextGen
