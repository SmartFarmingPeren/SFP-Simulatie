import numpy as np

SECTION_LENGTH: float = 2.0


class Section:
    def __init__(self, pos, direction, parent):
        self.pos: np.array = pos
        self.direction: np.array = direction
        self.orig_dir: np.array = direction
        self.thickness: int = 1
        self.count: int = 0
        self.parent = parent

    def next(self):
        # new_dir = self.direction + next_direction
        next_dir = self.direction * SECTION_LENGTH
        next_pos = self.pos + next_dir
        return Section(pos=next_pos, direction=self.direction, parent=self)

    def reset(self):
        self.direction = self.orig_dir
        self.count = 0