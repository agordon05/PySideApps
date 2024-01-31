import sys
from PySide6 import QtWidgets, QtCore, QtGui
from main_widget import Main_Widget
import stock_chart_widget
import stock_chart2 as stock


class Main_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = stock_chart_widget.StockChartWidget()
        # self.central_widget = stock.StockChartWidget()
        self.setCentralWidget(self.central_widget)

        self.refresh_button = QtWidgets.QPushButton('Refresh Chart')
        self.refresh_button.clicked.connect(self.refresh_chart)

        self.statusBar().addWidget(self.refresh_button)
        self.refresh_chart()

    def refresh_chart(self):
        self.central_widget.update_stock_chart()
        print("Refresh Chart Button Clicked")


def run_ui():
    app = QtWidgets.QApplication([])

    window = Main_Window()
    # window.resize(240, 150)
    window.resize(800, 600)
    window.setWindowTitle("Candle Chart")

    window.show()
    sys.exit(app.exec())
