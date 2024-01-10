from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from threading import Thread
import time

border_color: QtGui.QColor = QtGui.QColor(0, 0, 0)
default_button_color: Qt.GlobalColor = Qt.GlobalColor.gray
button_clicked_color: Qt.GlobalColor = Qt.GlobalColor.darkGray
button_color: Qt.GlobalColor = default_button_color


class Custom_Button(QtWidgets.QAbstractButton):
    update_signal = Signal(int)

    def __init__(self):
        super().__init__()
        self.count = 0
        self.label1 = QtWidgets.QLabel("label1")
        self.label2 = QtWidgets.QLabel("label2")
        self.label3 = QtWidgets.QLabel("label3")

        self.setLayout(QtWidgets.QHBoxLayout())
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        # self.h_layout = QtWidgets.QWidget()
        self.create_layout()
        self.add_functionality()

    def create_layout(self):
        # self.h_layout.setLayout(QtWidgets.QHBoxLayout())
        self.layout().addStretch()
        self.layout().addWidget(self.label1)
        self.layout().addStretch()
        self.layout().addWidget(self.label2)
        self.layout().addStretch()
        self.layout().addWidget(self.label3)
        self.layout().addStretch()
        # self.layout().addWidget(self.h_layout)

    def add_functionality(self):
        self.clicked.connect(self.button_clicked)
        self.pressed.connect(self.button_pressed)
        self.released.connect(self.button_released)

    @QtCore.Slot()
    def button_clicked(self):
        print("button clicked")

    @QtCore.Slot()
    def button_pressed(self):
        global button_clicked_color, button_color
        print("button pressed")
        button_color = button_clicked_color
        self.repaint()

    @QtCore.Slot()
    def button_released(self):
        global default_button_color, button_color
        print("button released")
        button_color = default_button_color
        self.repaint()

    def paintEvent(self, event):
        global border_color, button_color

        # rect = event.rect()

        painter = QtGui.QPainter(self)
        # painter.fillRect(rect, button_color)

        # painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)

        # Example: Custom drawing for a rounded rectangular button
        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.setPen(QtGui.QPen(border_color, 2))
        painter.setBrush(button_color)
        painter.drawRoundedRect(rect, 10, 10)
