from ProcessManager import ProcessManager

from utils.CONFIGFILE import AMOUNT_OF_TREES


def main():
    manager = ProcessManager(AMOUNT_OF_TREES)
    manager.grow_tree()


if __name__ == '__main__':
    main()
