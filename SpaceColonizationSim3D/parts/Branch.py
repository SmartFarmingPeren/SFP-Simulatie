import numpy as np
from typing import List

from parts.Section import Section

SECTION_LENGTH = 2


class Branch:
    def __init__(self, color = (0.0, 0.0, 0.0), parent: 'Branch' = None):
        # First section is at the start of the branch, last section is at the end
        self.sections: List[Section] = []
        self.children: List[Branch] = []
        self.parent: Branch = parent
        self.thickness: int = 1
        self.color: np.array = color
        self.should_grow: bool = False
        self.next_direction: np.array = np.array([0.0, 0.0, 0.0])

    # this method returns a new branch and makes it a child
    def next(self, section):
        new_branch = Branch(color=self.color, parent=self)
        new_branch.sections.append(section)
        self.children.append(new_branch)
        return new_branch

    def add_section(self):
        self.sections.append(self.get_last_section().next())

    # recursive loop through all branches and sections to get all points
    def get_points_to_save(self, points):
        print("[P:")
        for section in self.sections:
            points.append([section.pos[0], section.pos[1], section.pos[2]])
        for child in self.children:
            child_points = child.get_points_to_save(points)
        return points

    #
    # def reset(self):
    #     self.direction = self.orig_direction
    #     self.count = 0

    # def add_thickness(self):
    #     for section in self.sections:
    #         section.thickness += 1
    #     # self.thickness += 1
    #     # if self.parent is not None:
    #     #     self.parent.add_thickness()

    def get_first_section(self):
        if len(self.sections) > 0:
            return self.sections[0]
        else:
            return None

    def get_last_section(self):
        if len(self.sections) > 0:
            return self.sections[len(self.sections) - 1]
        else:
            return None

    def get_first_pos(self):
        section = self.get_first_section()
        if isinstance(section, Section):
            return section.pos
        else:
            return 0.0, 0.0, 0.0

    def get_last_pos(self):
        section = self.get_last_section()
        if isinstance(section, Section):
            return section.pos
        else:
            return 0.0, 0.0, 0.0

    # def subdivide(self):
    #     for i in range(len(self.sections)):
    #         other_i = i - 1
    #         if other_i >= 0:
    #             section = self.sections[i]
    #             other_section = self.sections[other_i]
    #             extra = Section(section.pos - other_section.pos, section.direction)
    #             self.sections.insert(i, extra)