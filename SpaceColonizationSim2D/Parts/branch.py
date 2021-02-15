class Branch:
    def __init__(self, pos, direction, last, color=None, parent=None):
        self.pos = pos
        self.origDirection = direction
        self.direction = self.origDirection
        self.parent = parent
        self.count = 0
        self.length = 10
        self.last = last
        self.color = color

    def next(self):
        nextDir = self.direction * self.length
        nextPos = self.pos + nextDir
        self.last = False
        return Branch(nextPos, self.direction, not self.last, parent=self)

    def reset(self):
        self.direction = self.origDirection
        self.count = 0
