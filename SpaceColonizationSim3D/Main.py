from ProcessManager import ProcessManager
from utils import IO


def main():
    # IO.view()
    manager = ProcessManager(1)
    manager.grow_tree()


if __name__ == '__main__':
    main()
