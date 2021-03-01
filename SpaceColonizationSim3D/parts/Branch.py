class Branch:
    def __init__(self, pos, direction, last, color=None, parent=None):
        self.pos = pos
        self.orig_direction = direction
        self.direction = self.orig_direction
        self.parent = parent
        self.count = 0
        self.length = 2
        self.last = last
        self.color = color
        self.thiccness = 1

    def next(self):
        next_dir = self.direction * self.length
        next_pos = self.pos + next_dir
        self.last = False
        self.color = "brown"
        self.add_thiccness()
        self.child = Branch(pos=next_pos, direction=self.direction, last=True, color="blue", parent=self)
        return self.child

    def reset(self):
        self.direction = self.orig_direction
        self.count = 0
    
    def add_thiccness(self):
        self.thiccness += 1
        if self.parent is not None:
            self.parent.add_thiccness()
