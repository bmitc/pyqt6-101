from PyQt6.QtWidgets import QApplication, QWidget

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.setWindowTitle("Simple example 1")
        self.resize(500, 500)
        self.show()


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec())
