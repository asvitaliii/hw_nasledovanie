import sys
from PyQt5.QtWidgets import QApplication
from gui import Manager


def main():
    app = QApplication([])
    win = Manager()
    win.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
