import sys
from PySide6 import QtWidgets
import main_window

app = QtWidgets.QApplication()
# window = main_window.Main_Window()


def run_ui():
    window = main_window.Main_Window()
    window.setFixedSize(600, 400)
    window.setWindowTitle("Custom Button")
    window.show()

    sys.exit(app.exec())
