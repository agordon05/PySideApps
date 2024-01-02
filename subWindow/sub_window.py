from PySide6 import QtWidgets, QtGui
from sub_widget import Sub_Widget

is_open = False
# __sub_window = None


class Sub_Window(QtWidgets.QWidget):

    def __init__(self):
        global is_open
        super().__init__()
        self.setObjectName("Sub_Window")
        self.widget = Sub_Widget()
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.widget)
        is_open = True
        # __sub_window = self

    def get_widget(self):
        return self

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        global is_open
        print("sub window Close event called")
        is_open = False
        super().closeEvent(event)


# def close_sub_window():
#     global __sub_window, is_open
#     print(f"{__sub_window}")
#     if __sub_window and is_open:
#         print("destroying sub window")
#         __sub_window.destroy()
#     else:
#         print("sub window is not set")
