from PySide6 import QtWidgets, QtGui, QtCore
from exchange import exchange

headers_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.gray
clicked_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.green
green_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.darkGreen
red_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.red
yellow_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.yellow


class Custom_Table(QtWidgets.QTableWidget):

    def __init__(self, headers: [str] = None, data: [exchange] = None):
        super().__init__()
        if data is None:
            data = []
        if headers is None:
            headers = []

        print(headers)
        print(data)
        self.data = data
        self.sort()

        # self.setLayout(QtWidgets.QVBoxLayout())
        # self.setColumnCount(5)
        # self.table = QtWidgets.QTableWidget()
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(headers)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.verticalHeader().hide()
        self.verticalHeader().setDefaultSectionSize(60)  # Set the default row height
        # self.setSortingEnabled(True)  # Enable sorting

        # self.horizontalHeader().setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.)

        self.__add_data()
        self.__add_functionality()
        self.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.SingleSelection)
        # Override the selection model to disable row selection
        # self.setSelectionModel(NoSelectionModel(self))
        # self.layout().addWidget(self.table)
        self.setShowGrid(False)

        self.setStyleSheet('''
            QTableWidget {
                background-color: lightgray;  /* Set the background color for the entire table */
            }
        
            QTableWidget::item {
                border-bottom: 1px solid #000000;  /* Set the border between cells */
            }
        
            QTableWidget::item:selected {
                background-color: darkgray;  /* Set the background color for selected cells */
            }
        ''')

    def __add_data(self):
        global green_color, red_color, yellow_color
        current_row_count = self.rowCount()

        for row, item in enumerate(self.data):
            if row >= current_row_count:
                self.setRowCount(row + 1)

            # create table cell
            status = self.item(row, 0) or QtWidgets.QTableWidgetItem()
            exchange_item = self.item(row, 1) or QtWidgets.QTableWidgetItem()
            name = self.item(row, 2) or QtWidgets.QTableWidgetItem()
            usdt = self.item(row, 3) or QtWidgets.QTableWidgetItem()
            profit = self.item(row, 4) or QtWidgets.QTableWidgetItem()

            # set text for table cell
            status.setText(item.status)
            exchange_item.setText(item.exchange)
            name.setText(item.name)
            usdt.setText(f"${item.usdt}")
            profit.setText(f"${item.profit}")

            if item.status == "Active":
                status.setForeground(QtGui.QBrush(green_color))
            elif item.status == "Closed" or item.status == "Inactive":
                status.setForeground(QtGui.QBrush(red_color))
            else:
                status.setForeground(QtGui.QBrush(yellow_color))

            if row >= current_row_count:

                profit.setForeground(QtGui.QBrush(green_color))

                # align table cell
                status.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
                exchange_item.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
                name.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
                usdt.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
                profit.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)

                font = QtGui.QFont()
                font.setPointSize(18)

                status.setFont(font)
                exchange_item.setFont(font)
                name.setFont(font)
                usdt.setFont(font)
                profit.setFont(font)

                self.setRowHeight(row, 60)

                # add table cell
                self.setItem(row, 0, status)
                self.setItem(row, 1, exchange_item)
                self.setItem(row, 2, name)
                self.setItem(row, 3, usdt)
                self.setItem(row, 4, profit)

    def __add_functionality(self):
        self.itemPressed.connect(self.__cell_pressed)
        self.itemClicked.connect(self.__row_clicked)

    def update_data(self, new_data: [exchange]):
        self.clearContents()
        self.setRowCount(0)
        self.data = new_data
        self.sort()
        self.__add_data()

    def refresh_data(self):
        # temp_order = self.get_data_order()
        # self.data = temp_order
        self.__add_data()

    # def get_data_order(self) -> [exchange]:
    #     data: [exchange] = []
    #     data_names: [str] = []
    #
    #     for row, item in enumerate(self.data):
    #         data_names.append(self.item(row, 2))
    #     print("data names gotten")
    #     # when applied to trading system. names will be unique
    #     for name in data_names:
    #         for exchange_o in self.data:
    #             if exchange_o.name == name:
    #                 data.append(exchange_o)
    #                 break
    #     print("done sorting through data")
    #     return data

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        # Override the default behavior to prevent selection dragging
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            return

        super(Custom_Table, self).mouseMoveEvent(event)

    def sort(self):
        pass
        # sort by Name
        self.data = sorted(self.data, key=lambda item: item.name)

        # sort by Exchange
        self.data = sorted(self.data, key=lambda item: item.exchange)

        # sort by Status
        status_order = {"Pending": 0, "Active": 1, "Inactive": 2, "Closed": 3}
        self.data = sorted(self.data, key=lambda item: status_order.get(item.status, float('inf')))


    @QtCore.Slot()
    def __row_clicked(self, item):
        row = item.row()
        # print(f"row {row} Clicked")
        data = self.data[row]
        data.button_click()
        # print(data)

    @QtCore.Slot()
    def __cell_pressed(self, item):
        # Get the row index of the clicked item
        row = item.row()
        # Set the entire row as selected
        for col in range(self.columnCount()):

            item = self.item(row, col)
            item.setSelected(True)


