from PySide6 import QtWidgets, QtGui, QtCore

headers_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.gray
row_default_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.gray
row_clicked_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.darkGray
row_color: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.gray
row_outline: QtGui.Qt.GlobalColor = QtGui.Qt.GlobalColor.black


class _Header(QtWidgets.QWidget):
    def __init__(self, data: [str] = None):
        super().__init__()
        if data is None:
            data = []
        self.setLayout(QtWidgets.QVBoxLayout())
        self.create_header(data)
        self.count = len(data)

    def create_header(self, data: [str]):
        hor_layout = QtWidgets.QWidget()
        hor_layout.setLayout(QtWidgets.QHBoxLayout())
        for col in data:
            label = QtWidgets.QLabel(col)
            hor_layout.layout().addStretch()
            hor_layout.layout().addWidget(label)
        hor_layout.layout().addStretch()
        # hor_layout.setFixedHeight(self.height())
        # self.layout().addStretch()
        self.layout().addWidget(hor_layout)
        # self.layout().addStretch()

    def paintEvent(self, event):
        global headers_color

        rect = event.rect()
        painter = QtGui.QPainter(self)

        painter.fillRect(rect, row_color)

        # painter = QtGui.QPainter(self)
        #
        # rect = self.rect().adjusted(1, 1, -1, -1)
        # painter.setPen(QtGui.QPen(headers_color, 2))
        # painter.setBrush(headers_color)
        # painter.drawRoundedRect(rect, 10, 10)


class _row(QtWidgets.QAbstractButton):
    def __init__(self, headers: _Header, row: [] = None):
        super().__init__()
        # self.setContentsMargins(0, 0, 0, 0)
        if row is None:
            return

        if len(row) > headers.count:
            return
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.setMaximumHeight(70)
        self.setMinimumHeight(0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(40)
        print(f"row before minimum size hint: {self.minimumSizeHint()}")
        print(f"row before minimum size: {self.minimumSize()}")
        print(f"row before size hint: {self.sizeHint()}")
        print(f"row before adjust size: {self.adjustSize()}")

        print(f"row before margin contents: {self.contentsMargins()}")
        print(f"row before rect contents: {self.contentsRect()}")
        print(f"row before heightMM: {self.heightMM()}")
        print(f"row before visible region: {self.visibleRegion()}")

        self.setLayout(QtWidgets.QVBoxLayout())

        self.create_row(row)
        # self.setMinimumHeight(0)

        print(f"row after minimum size hint: {self.minimumSizeHint()}")
        print(f"row after minimum size: {self.minimumSize()}")
        print(f"row after size hint: {self.sizeHint()}")
        print(f"row after adjust size: {self.adjustSize()}")

        print(f"row after margin contents: {self.contentsMargins()}")
        print(f"row after rect contents: {self.contentsRect()}")
        print(f"row after heightMM: {self.heightMM()}")
        print(f"row after visible region: {self.visibleRegion()}")
        self.add_functionality()

    def create_row(self, row: []):

        hor_layout = QtWidgets.QWidget()
        hor_layout.setLayout(QtWidgets.QHBoxLayout())
        hor_layout.setContentsMargins(0, 0, 0, 0)

        # hor_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)

        for item in row:
            label = QtWidgets.QLabel(item)
            label.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
            label.setMinimumSize(0, 0)
            label.setContentsMargins(0, 0, 0, 0)
            label.setFixedHeight(40)
            label.setAlignment(label.alignment().AlignTop)
            # hor_layout.layout().addStretch()
            hor_layout.layout().addWidget(label)
        # hor_layout.layout().addStretch()

        self.layout().addWidget(hor_layout)
        self.layout().setAlignment(self.layout().alignment().AlignTop)

    def add_functionality(self):
        self.clicked.connect(self.row_clicked)
        self.pressed.connect(self.row_pressed)
        self.released.connect(self.row_unpressed)

    def sizeHint(self):
        return QtCore.QSize(100, 40)  # Set your preferred width and height

    def paintEvent(self, event):
        global row_color, row_outline

        rect = event.rect()
        painter = QtGui.QPainter(self)

        painter.fillRect(rect, row_color)

        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.setPen(QtGui.QPen(row_outline, 2))
        # painter.setBrush(row_color)
        painter.drawRoundedRect(rect, 10, 10)

    @QtCore.Slot()
    def row_clicked(self):
        print("row clicked")
        pass

    @QtCore.Slot()
    def row_pressed(self):
        global row_color, row_clicked_color
        row_color = row_clicked_color
        self.repaint()

    def row_unpressed(self):
        global row_color, row_default_color
        row_color = row_default_color
        self.repaint()


class Custom_Table(QtWidgets.QWidget):

    def __init__(self, headers: [str] = None, data: [{}] = None):
        super().__init__()
        if data is None:
            data = []
        if headers is None:
            headers = []
        self.setLayout(QtWidgets.QVBoxLayout())
        headers = _Header(headers)
        # headers.setFixedWidth(self.width())
        # headers.setMaximumHeight(40)
        headers.update()
        # self.layout().addStretch()
        self.layout().addWidget(headers)
        for row_data in data:
            item1 = row_data['Status']
            item2 = row_data['Exchange']
            item3 = row_data['Name']
            item4 = f"${row_data['USDT']}"
            item5 = F"${row_data['Profit']}"
            row_data = [item1, item2, item3, item4, item5]
            row = _row(headers, row_data)
            # row.setMinimumSize(0, 0)
            row.setContentsMargins(0, 0, 0, 0)

            # row.setFixedHeight(50)
            print(row.size())

            # row.setFixedWidth(self.width())
            # row.setMaximumHeight(40)
            self.layout().addWidget(row)
        self.layout().addStretch()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        global row_color

        # rect = event.rect()
        painter = QtGui.QPainter(self)

        # painter.fillRect(rect, row_color)
        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.setPen(QtGui.QPen(row_color, 2))
        painter.setBrush(row_color)
        painter.drawRoundedRect(rect, 10, 10)
