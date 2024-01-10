from PySide6 import QtWidgets
import main_widget


class Main_Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        widget = main_widget.Main_Widget()
        # widget.setFixedSize(500, 350)
        widget.show()
        self.setCentralWidget(widget)
