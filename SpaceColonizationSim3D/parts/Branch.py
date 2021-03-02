class Branch:
    def __init__(self, pos, direction, last, parent=None):
        self.pos = pos
        self.orig_direction = direction
        self.direction = self.orig_direction
        self.parent = parent
        self.count = 0
        self.length = 2
        self.last = last
        self.thickness = 1

    def next(self):
        next_dir = self.direction * self.length
        next_pos = self.pos + next_dir
        self.last = False
        self.add_thickness()
        self.child = Branch(pos=next_pos, direction=self.direction, last=True, parent=self)
        return self.child

    def reset(self):
        self.direction = self.orig_direction
        self.count = 0
    
    def add_thickness(self):
        self.thickness += 1
        if self.parent is not None:
            self.parent.add_thickness()
