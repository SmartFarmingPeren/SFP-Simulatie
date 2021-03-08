import numpy as np
from typing import List

from parts.Section import Section

SECTION_LENGTH = 2


class Branch:
    def __init__(self, direction, position, parent: 'Branch' = None):
        # First section is at the start of the branch, last section is at the end
        self.sections: List[Section] = []
        self.children: List[Branch] = []
        self.parent: Branch = parent if parent is not None else None
        self.thickness = 1
        self.should_grow: bool = False
        self.next_direction: np.array = np.array([0.0, 0.0, 0.0])
        self.sections.append(Section(direction, position))

    def grow(self):
        for section in reversed(self.sections):
            if section.can_grow:
                new_section = self.next_section(self.next_direction)
                self.sections.append(new_section)
                section.can_grow = False

    def add_section(self):
        self.sections.append(self.get_last_section().next(self.next_direction))

    # Returns the next section based on current section's postion, length and direction
    def next_section(self, next_direction: np.array):
        if len(self.sections) < 1:
            if self.parent is not None:
                cur_section = self.parent.get_last_section()
            else:
                cur_section = Section([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
        else:
            cur_section = self.sections[len(self.sections) - 1]

        new_dir = cur_section.direction + next_direction
        translation = new_dir * SECTION_LENGTH
        next_pos = cur_section.pos + translation
        next_section = Section(pos=next_pos, direction=cur_section.direction)
        return next_section

    # recursive loop through all branches and sections to get all points
    def get_points_to_save(self, points):
        for section in self.sections:
            points.append([section.pos[0], section.pos[1], section.pos[2]])
        if len(self.children) > 0:
            for child in self.children:
                child_points = child.get_points_to_save(points)
                for point in child_points:
                    points.append(point)
        return points
    #
    # def reset(self):
    #     self.direction = self.orig_direction
    #     self.count = 0
    
    def add_thickness(self):
        self.thickness += 1
        if self.parent is not None:
            self.parent.add_thickness()

    def add_child_branch(self, branch: 'Branch'):
        self.children.append(branch)

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
