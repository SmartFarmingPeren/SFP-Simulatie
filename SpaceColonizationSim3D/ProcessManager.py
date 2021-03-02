from utils.Process import TreeProcess

# Creates tree processes
class Manager:
    # generation is how many trees you want
    def __init__(self, amount_of_trees=0):
        self.amount_of_trees = amount_of_trees

    def grow_tree(self):
        for _ in range(self.amount_of_trees):
            process = TreeProcess()
            process.start()
