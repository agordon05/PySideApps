import sys
from PySide6 import QtWidgets
import main_window

app = QtWidgets.QApplication()
window: main_window.Main_Window = main_window.Main_Window()


def run_ui():
    global app
    create_window()
    sys.exit(app.exec())


def create_window():
    global window

    window.resize(600, 400)
    window.setWindowTitle("widget switch")
    window.show()


def switch_widget(widget: QtWidgets.QWidget):
    global window
    window.setCentralWidget(widget)

