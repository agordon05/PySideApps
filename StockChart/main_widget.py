from PySide6 import QtWidgets, QtCore, QtGui
import stock_chart_widget

class Main_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create objects
        self.count: int = 0
        self.text = QtWidgets.QLabel(f"{self.count}")
        self.button = QtWidgets.QPushButton()

        # style text
        font = QtGui.QFont()
        font.setPointSize(20)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # style button
        # self.button.setText("Click me!")
        # self.button.setFixedSize(200, 60)
        self.stock_chart = stock_chart_widget.StockChartWidget()
        # create layout
        # self.top_widget = QtWidgets.QWidget()
        # self.create_top_layout()

        self.bottom_widget = QtWidgets.QWidget()
        self.create_bottom_layout()

        self.merge_layouts()

        # set actions
        # self.button.clicked.connect(self.button_click)

    # # set actions
    # @QtCore.Slot()
    # def button_click(self):
    #     self.count += 1
    #     self.text.setText(f"{self.count}")

    # sets the layout for the top side of widget
    # def create_top_layout(self):
    #     self.top_widget.setLayout(QtWidgets.QHBoxLayout())
    #     self.top_widget.layout().addStretch()
    #     self.top_widget.layout().addWidget(self.text)
    #     self.top_widget.layout().addStretch()

    # sets the layout for the bottom side of widget
    def create_bottom_layout(self):
        self.bottom_widget.setLayout(QtWidgets.QHBoxLayout())
        self.bottom_widget.layout().addStretch()
        self.bottom_widget.layout().addWidget(self.stock_chart)
        self.bottom_widget.layout().addStretch()

    # merges both the top side widget and the bottom side widget into a single widget
    def merge_layouts(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        # self.layout().addStretch()
        # self.layout().addWidget(self.top_widget)
        self.layout().addStretch()
        self.layout().addWidget(self.bottom_widget)
        self.layout().addStretch()
