from PySide6 import QtWidgets, QtCore
import window_controller
import main_widget
import tertiary_widget


class Second_Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel("Second Widget")

        self.next_button = QtWidgets.QPushButton("Next")
        self.next_button.setFixedSize(200, 200)
        self.next_button.clicked.connect(self.next_button_click)

        self.prev_button = QtWidgets.QPushButton("Prev")
        self.prev_button.setFixedSize(200, 200)
        self.prev_button.clicked.connect(self.prev_button_click)

        self.horizontal_layout = QtWidgets.QWidget()
        self.create_horizontal_layout()

        self.setLayout(QtWidgets.QVBoxLayout())

        self.layout().addStretch()
        self.layout().addWidget(self.label)
        self.layout().addStretch()
        self.layout().addWidget(self.horizontal_layout)
        self.layout().addStretch()

    @QtCore.Slot()
    def next_button_click(self):
        print("button clicked")
        window_controller.switch_widget(tertiary_widget.Third_Widget())

    @QtCore.Slot()
    def prev_button_click(self):
        print("button clicked")
        window_controller.switch_widget(main_widget.Main_Widget())

    def create_horizontal_layout(self):
        self.horizontal_layout.setLayout(QtWidgets.QHBoxLayout())
        self.horizontal_layout.layout().addStretch()
        self.horizontal_layout.layout().addWidget(self.prev_button)
        self.horizontal_layout.layout().addStretch()
        self.horizontal_layout.layout().addWidget(self.next_button)
        self.horizontal_layout.layout().addStretch()
