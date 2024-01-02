import sys
from PySide6 import QtWidgets

import sub_window
from main_widget import Main_Widget


class Main_Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # create widget
        self.widget = Main_Widget()

        # add to central widget
        self.setCentralWidget(self.widget)

        # self.sub_window = None

    # def closeEvent(self, event):
    #     print("close event called")
    #     # Close the sub window if it exists
    #     if sub_window.is_open:
    #         print("sub window exists")
    #         sub_window.close_sub_window()
    #     event.accept()  # Allow the main window to close


def run_ui():
    app = QtWidgets.QApplication([])
    window = Main_Window()
    window.setWindowTitle("New Window App")
    # window.resize(150, 300)
    window.setFixedSize(400, 200)
    window.show()
    sys.exit(app.exec())
