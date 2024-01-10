import time
import threading
from PySide6 import QtWidgets, QtCore, QtGui
import custom_table
import window_controller
from exchange import exchange

table_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.gray

class Main_Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel("label")

        headers = self.create_temp_headers()
        self.row_data = self.create_temp_data()

        self.setContentsMargins(0, 0, 0, 0)
        self.custom_table = custom_table.Custom_Table(headers=headers, data=self.row_data)
        window_controller.new_table(self.custom_table)
        # self.custom_table.setFixedSize(700, 400)  # Adjust the size as needed
        self.h_layout = QtWidgets.QWidget()

        self.create_horizontal_layout()
        self.create_vertical_layout()

        thread = threading.Thread(target=self.changeValue)
        # thread2 = threading.Thread(target=self.add_exchange)
        # thread3 = threading.Thread(target=self.remove_exchange)
        thread.start()
        # thread2.start()
        # thread3.start()


    def create_horizontal_layout(self):
        self.h_layout.setLayout(QtWidgets.QHBoxLayout())
        # self.h_layout.layout().addStretch()
        self.h_layout.layout().addWidget(self.custom_table)
        # self.h_layout.layout().addWidget(self.custom_button)
        # self.h_layout.layout().addStretch()

    def create_vertical_layout(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        # self.layout().addStretch()
        self.layout().addWidget(self.h_layout)
        # self.layout().addStretch()

    def paintEvent(self, event):
        global table_color

        rect = event.rect()
        painter = QtGui.QPainter(self)

        painter.fillRect(rect, table_color)

        # rect = self.rect().adjusted(1, 1, -1, -1)
        # painter.setPen(QtGui.QPen(table_color, 2))
        # # painter.setBrush(row_color)
        # painter.drawRoundedRect(rect, 10, 10)

    def create_temp_headers(self) -> [str]:
        headers: [str] = ["Status", "Exchange", "Name", "USDT", "Profit"]
        return headers

    def create_temp_data(self) -> []:
        exchange1 = exchange("Active", "BinanceUS", "Personal", 123.2, 12.32)
        exchange2 = exchange("Inactive", "Bitmex", "Business", 1234.21, 123.21)
        exchange3 = exchange("Closed", "Stock", "investments", 26000.12, 1000.12)
        exchange4 = exchange("Pending", "Stock", "investments", 26000.12, 1000.12)
        exchange5 = exchange("Active", "Acoi", "Testing", 12543.12, 513.12)

        return [exchange1, exchange2, exchange3, exchange4, exchange5, exchange1, exchange2, exchange3, exchange4,
                exchange5, exchange1, exchange2, exchange3, exchange4, exchange5, exchange1, exchange2, exchange3,
                exchange4, exchange5]

    def changeValue(self):
        while True:
            time.sleep(3)
            # print("Changing status")
            if self.row_data[0].status == "Active":
                self.row_data[0].status = "Inactive"
            elif self.row_data[0].status == "Inactive":
                self.row_data[0].status = "Closed"
            elif self.row_data[0].status == "Closed":
                self.row_data[0].status = "Pending"
            elif self.row_data[0].status == "Pending":
                self.row_data[0].status = "Active"
            # print(self.row_data[0].status)
            window_controller.update_table()

    # def add_exchange(self):
    #     while True:
    #         time.sleep(5)
    #         exchange2 = exchange("Inactive", "Bitmex", "Business", 1234.21, 123.21)
    #         self.row_data.append(exchange2)
    #         window_controller.update_table(data=self.row_data)
    #
    # def remove_exchange(self):
    #     while True:
    #         time.sleep(16)
    #         self.row_data.remove(self.row_data[2])
    #         window_controller.update_table(data=self.row_data)
