from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.setWindowTitle("Simple example 2")
        self.resize(500, 500)
        # self.setWindowIcon(QIcon(""))

        button_click = QPushButton(parent=self)
        button_click.setText("Quit")
        button_click.move(100, 100)
        button_click.clicked.connect(QApplication.instance().quit)

        self.show()


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec())
