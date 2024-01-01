# Used https://www.youtube.com/watch?v=Cqo0-EQmy1Q&ab_channel=QtGroup for tutorial

import sys
from PySide6 import QtCore, QtWidgets, QtGui


class myWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create objects
        self.button = QtWidgets.QPushButton("click to display text")
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Enter to append")
        self.text_edit = QtWidgets.QTextEdit()

        # add to Widget layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text_edit)

        # set method to button
        self.button.clicked.connect(self.button_click)

    @QtCore.Slot()
    def button_click(self):
        self.text_edit.append(self.line_edit.text())
        self.line_edit.setText("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = myWidget()
    widget.resize(800, 600)
    widget.show()
    widget.setWindowTitle("Intro to Pyside")

    sys.exit(app.exec())
