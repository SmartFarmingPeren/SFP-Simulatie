from utils import IO
from utils.TreeProcess import TreeProcess


# Creates tree processes
class ProcessManager:
    def __init__(self, amount_of_trees=1):
        self.amount_of_trees = amount_of_trees

    def grow_tree(self):
        for _ in range(self.amount_of_trees):
            process = TreeProcess()
            process.start()
