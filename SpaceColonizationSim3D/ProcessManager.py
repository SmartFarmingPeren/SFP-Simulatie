from utils.Process import TreeProcess

PointSize = 2 / 2


# Creates tree processes
class Manager:
    # generation is how many trees you want
    def __init__(self, generation=0):
        self.generation = generation

    def grow_tree(self):
        i = 0
        while i < self.generation:
            process = TreeProcess()
            process.start()
            i += 1
