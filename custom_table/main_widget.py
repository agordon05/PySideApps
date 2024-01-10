from PySide6 import QtWidgets, QtCore, QtGui
import custom_table


class Main_Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel("label")
        headers = self.create_temp_headers()
        row_data = self.create_temp_data()
        self.custom_table = custom_table.Custom_Table(headers=headers, data=row_data)
        # self.custom_table.setMaximumHeight(400)
        # self.custom_table.setMaximumWidth(400)
        # print(self.custom_table.size())
        self.custom_table.setFixedWidth(700)
        # self.custom_button.setFixedSize(100, 50)  # Adjust the size as needed
        self.h_layout = QtWidgets.QWidget()

        self.create_horizontal_layout()
        self.create_vertical_layout()

    def create_horizontal_layout(self):
        self.h_layout.setLayout(QtWidgets.QHBoxLayout())
        self.h_layout.layout().addStretch()
        self.h_layout.layout().addWidget(self.custom_table)
        # self.h_layout.layout().addWidget(self.custom_button)
        self.h_layout.layout().addStretch()

    def create_vertical_layout(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addStretch()
        self.layout().addWidget(self.h_layout)
        self.layout().addStretch()

    def paintEvent(self, event):
        global row_color, row_outline

        rect = event.rect()
        painter = QtGui.QPainter(self)

        painter.fillRect(rect, row_color)

        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.setPen(QtGui.QPen(row_outline, 2))
        # painter.setBrush(row_color)
        painter.drawRoundedRect(rect, 10, 10)

    def create_temp_headers(self) -> [str]:
        headers: [str] = ["Status", "Exchange", "Name", "USDT", "Profit"]
        return headers

    def create_temp_data(self) -> [{}]:
        row = {
            'Status': "Active",
            'Exchange': "BinanceUS",
            'Name': "Personal",
            'USDT': 123.2,
            'Profit': 12.32
        }
        row2 = {
            'Status': "Inactive",
            'Exchange': "Bitmex",
            'Name': "Business",
            'USDT': 1234.21,
            'Profit': 123.21
        }
        row3 = {
            'Status': "Closed",
            'Exchange': "Stock",
            'Name': "investments",
            'USDT': 26000.12,
            'Profit': 1000.12
        }
        row4 = {
            'Status': "Closed",
            'Exchange': "Stock",
            'Name': "investments",
            'USDT': 26000.12,
            'Profit': 1000.12
        }
        return [row, row2, row3, row4]
