from typing import List

import numpy as np

from parts.Section import Section

SECTION_LENGTH = 2


class Branch:
    def __init__(self, level, color, parent: 'Branch' = None):
        # First section is at the start of the branch, last section is at the end
        self.sections: List[Section] = []
        self.children: List[Branch] = []
        self.parent: Branch = parent
        self.color: np.array = color
        self.level = level

    # this method returns a new branch and makes it a child
    def next(self, section):
        new_color = self.color / [self.level + 1, self.level + 0.5, self.level + .25]
        new_branch = Branch(level=self.level + 1, color=new_color, parent=self)
        new_branch.sections.append(section)
        self.children.append(new_branch)
        return new_branch

    def add_section(self):
        self.sections.append(self.get_last_section().next())

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
        return self.get_first_section().pos

    def get_last_pos(self):
        return self.get_last_section().pos

    # def subdivide(self):
    #     for i in range(len(self.sections)):
    #         other_i = i - 1
    #         if other_i >= 0:
    #             section = self.sections[i]
    #             other_section = self.sections[other_i]
    #             extra = Section(section.pos - other_section.pos, section.direction)
    #             self.sections.insert(i, extra)


def get_next(node):
    yield node
    for child in node.children:
        yield from get_next(child)
