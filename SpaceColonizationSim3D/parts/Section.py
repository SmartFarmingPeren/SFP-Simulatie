import numpy as np

SECTION_LENGTH: float = 2.0


class Section:
    def __init__(self, pos, direction, parent, thickness=1):
        self.pos: np.array = pos
        self.direction: np.array = direction
        self.orig_dir: np.array = direction
        self.thickness: int = thickness
        self.count: int = 0
        self.parent = parent

    def next(self):
        # new_dir = self.direction + next_direction
        next_dir = self.direction * SECTION_LENGTH
        next_pos = self.pos + next_dir
        self.add_thickness()
        return Section(pos=next_pos, direction=self.direction, parent=self)

    def reset(self):
        self.direction = self.orig_dir
        self.count = 0

    def add_thickness(self):
        self.thickness += 1
        if self.parent is not None:
            self.parent.add_thickness()
