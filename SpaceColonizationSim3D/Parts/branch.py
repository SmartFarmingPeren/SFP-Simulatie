class Branch:
    def __init__(self, pos, direction, last, color=None, parent=None):
        self.pos = pos
        self.origDirection = direction
        self.direction = self.origDirection
        self.parent = parent
        self.count = 0
        self.length = 2
        self.last = last
        self.color = color
        self.Thickness = 1

    def next(self):
        nextDir = self.direction * self.length
        #print(self.direction)
        #print(nextDir)
        nextPos = self.pos + nextDir
        self.last = False
        self.color = "brown"
        self.addAThickness()
        self.child = Branch(pos=nextPos, direction=self.direction, last=True, color="blue", parent=self)
        return self.child

    def reset(self):
        self.direction = self.origDirection
        self.count = 0
    
    def addAThickness(self):
        self.Thickness += 1
        if self.parent is not None:
            self.parent.addAThickness()
