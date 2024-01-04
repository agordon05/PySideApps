from PySide6 import QtWidgets, QtCore, QtGui
import window_controller


class Main_Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel("main Widget")

        self.button = QtWidgets.QPushButton("Next")
        self.button.setFixedSize(200, 200)
        self.button.clicked.connect(self.button_click)

        self.horizontal_layout = QtWidgets.QWidget()
        self.create_horizontal_layout()

        self.setLayout(QtWidgets.QVBoxLayout())

        self.layout().addStretch()
        self.layout().addWidget(self.label)
        self.layout().addStretch()
        self.layout().addWidget(self.horizontal_layout)
        self.layout().addStretch()



    @QtCore.Slot()
    def button_click(self):
        print("button clicked")
        from secondary_widget import Second_Widget
        window_controller.switch_widget(Second_Widget())

    def create_horizontal_layout(self):
        self.horizontal_layout.setLayout(QtWidgets.QHBoxLayout())
        self.horizontal_layout.layout().addStretch()
        self.horizontal_layout.layout().addWidget(self.button)
        self.horizontal_layout.layout().addStretch()
