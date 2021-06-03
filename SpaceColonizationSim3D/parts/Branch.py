from typing import List

from parts.Section import Section

SECTION_LENGTH = 2

COLORS = [[0.0, 0.0, 0.0],  # Age 0 = BLACK
          [0.0, 1.0, 0.0],  # Age 1 = GREEN
          [1.0, 1.0, 0.0],  # Age 2 = YELLOW
          [1.0, 0.0, 0.0],  # Age 3 = RED
          [0.0, 0.0, 1.0]]  # Age 4 = BLUE


class Branch:
    def __init__(self, age, parent: 'Branch' = None):
        # First section is at the start of the branch, last section is at the end
        self.sections: List[Section] = []
        self.children: List[Branch] = []
        self.parent: Branch = parent
        self.age = age

    def next(self, section: Section):
        """
        Creates a new branch with age 1 and gives it the first section
        :rtype: Returns the newly generated branch
        """
        for sec in self.sections:
            print(sec)
        new_branch = Branch(age=1, parent=self)
        new_branch.sections.append(section)
        self.children.append(new_branch)
        return new_branch

    def add_section(self):
        """
        Adds a new section to an existing branch
        """
        self.sections.append(self.get_last_section().next())

    def return_color(self):
        """
        This function is used to return the color of the branch
        :rtype: It returns the exact color of the branch
        """
        return COLORS[self.age] if self.age <= 4 else COLORS[0]

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
        """
        Goes to the first section of a branch
        :rtype: Returns either the first section or nothing because you already are at the first section
        """
        if len(self.sections) > 0:
            return self.sections[0]
        else:
            return None

    def get_last_section(self):
        """
        Goes to the last section of the branch
        :rtype: Returns either the last section or none because you already are at the last section
        """
        if len(self.sections) > 0:
            return self.sections[len(self.sections) - 1]
        else:
            return None

    def get_first_pos(self):
        """
        :rtype: Returns the first coordinate of a section
        """
        return self.get_first_section().pos

    def get_last_pos(self):
        """
        :rtype: Returns the last coordinate of a section
        """
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