class Branch:
    def __init__(self, pos, direction, last, color=None, parent=None):
        self.pos = pos
        self.origDirection = direction
        self.direction = self.origDirection
        self.parent = parent
        self.count = 0
        self.length = 1
        self.last = last
        self.color = color

    def next(self):
        nextDir = self.direction * self.length
        nextPos = self.pos + nextDir
        self.last = False
        self.color = "brown"
        return Branch(pos=nextPos, direction=self.direction, last=True, color="blue", parent=self)

    def reset(self):
        self.direction = self.origDirection
        self.count = 0
