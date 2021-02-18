class Branch:
    next_id = 0
    def __init__(self, pos, direction, last, color="brown", parent=None):
        self.pos = pos
        self.origDirection = direction
        self.direction = self.origDirection
        self.parent = parent
        self.count = 0
        self.length = 5  # branch length
        self.last = last
        self.color = color
        self.age = 0
        self.branchid = Branch.next_id
        Branch.next_id += 1

    def next(self):
        nextDir = self.direction * self.length
        nextPos = self.pos + nextDir
        self.last = False
        self.color = "yellow"
        self.ColorCheck()
        return Branch(pos=nextPos, direction=self.direction, last=True, color=self.color, parent=self)

    def ColorCheck(self):
        self.age += 1
        #print(self.age, " ", self.branchid)
        if self.age > 4:
            self.color = "green"
        if self.age > 10:
            self.color = "yellow"

    def reset(self):
        self.direction = self.origDirection
        self.count = 0
