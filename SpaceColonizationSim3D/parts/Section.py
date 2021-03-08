import numpy as np

SECTION_LENGTH: float = 2.0


class Section:
    def __init__(self, pos: np.array, direction: np.array):
        self.pos: np.array = pos
        self.direction: np.array = direction
        self.thickness: int = 1
        self.can_grow: bool = False

    def next(self, next_direction: np.array):
        # new_dir = self.direction + next_direction
        translation = self.direction * SECTION_LENGTH
        next_pos = self.pos + translation
        return Section(pos=next_pos, direction=self.direction)
