from PySide6 import QtWidgets, QtCore
import custom_button


class Main_Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel("label")

        self.custom_button = custom_button.Custom_Button()
        # self.custom_button.setFixedSize(100, 50)  # Adjust the size as needed
        self.h_layout = QtWidgets.QWidget()

        self.create_horizontal_layout()
        self.create_vertical_layout()

    def create_horizontal_layout(self):
        self.h_layout.setLayout(QtWidgets.QHBoxLayout())
        self.h_layout.layout().addStretch()
        self.h_layout.layout().addWidget(self.custom_button)
        # self.h_layout.layout().addWidget(self.custom_button)
        self.h_layout.layout().addStretch()

    def create_vertical_layout(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addStretch()
        self.layout().addWidget(self.h_layout)
        self.layout().addStretch()

