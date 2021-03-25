import numpy as np

from utils.CONFIGFILE import ADD_THICKNESS_VALUE, THRESHOLD, SECTION_LENGTH


class Section:
    def __init__(self, pos, direction, parent, thickness=1):
        self.pos: np.array = pos
        self.direction: np.array = direction
        self.orig_dir: np.array = direction
        self.thickness: int = thickness
        self.count: int = 0
        self.parent = parent

    def next(self):
        """
        This function is used to determine the next position of a section of the tree.
        :rtype: It returns a section with a position and a direction
        """
        # new_dir = self.direction + next_direction
        next_dir = self.direction * SECTION_LENGTH
        for count in range(0, 3):
            if next_dir[count] > THRESHOLD:
                next_dir[count] = THRESHOLD
            if next_dir[count] < -THRESHOLD:
                next_dir[count] = -THRESHOLD
        next_pos = self.pos + next_dir
        self.add_thickness()
        return Section(pos=next_pos, direction=self.direction, parent=self)

    def reset(self):
        """
        This function is used to reset the direction of a section
        """
        self.direction = self.orig_dir
        self.count = 0

    def add_thickness(self):
        """
        With this function the thickness of the previous section is increased so the older the branch to thicker it gets
        """
        self.thickness += ADD_THICKNESS_VALUE
        if self.parent is not None:
            self.parent.add_thickness()

    def __str__(self):
        return "Section; position: [%.2f, %.2f, %.2f]" % (self.pos[0], self.pos[1], self.pos[2])
