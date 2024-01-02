from PySide6 import QtWidgets, QtCore
import sub_window


class Main_Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click to open Window")
        self.button.setFixedSize(350, 150)
        self.button.clicked.connect(self.on_clicked)

        self.container = QtWidgets.QWidget()
        self.container.setLayout(QtWidgets.QHBoxLayout())
        self.container.layout().addStretch()
        self.container.layout().addWidget(self.button)
        self.container.layout().addStretch()

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.container)
        self.sub_window = None

    @QtCore.Slot()
    def on_clicked(self):

        if sub_window.is_open:
            print("sub window exists")
            return

        else:
            print("sub window does not exist")

        window = sub_window.Sub_Window()
        window.setGeometry(100, 100, 240, 150)  # Adjust the coordinates as needed
        window.show()

        # ensures sub window stays open
        self.sub_window = window

    #     window.destroyed.connect(self.destroy_sub_window)
    #
    # def destroy_sub_window(self):
    #     print("sub window destroyed")
    #     self.sub_window = None

