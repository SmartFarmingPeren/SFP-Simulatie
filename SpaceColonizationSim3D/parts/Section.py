import numpy as np

SECTION_LENGTH: float = 2.0


class Section:
    def __init__(self, pos: np.array, direction: np.array):
        self.pos: np.array = pos
        self.direction: np.array = direction
        self.thickness = 1
        self.can_grow = False

    def next(self, next_direction: np.array):
        new_dir = self.direction + next_direction
        translation = new_dir * SECTION_LENGTH
        next_pos = self.pos + translation
        return Section(pos=next_pos, direction=new_dir)
