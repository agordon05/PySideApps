import sys
from PySide6 import QtWidgets, QtCore, QtGui
from main_widget import Main_Widget


class Main_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = Main_Widget()
        self.setCentralWidget(self.widget)


def run_ui():
    app = QtWidgets.QApplication([])

    window = Main_Window()
    window.resize(200, 150)
    window.setWindowTitle("Intro 2")

    window.show()
    sys.exit(app.exec())
