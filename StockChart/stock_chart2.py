import sys
import random
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg


class StockChartWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # Create a PlotWidget
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)

        self.create_stock_chart()

    def create_stock_chart(self):
        # For demonstration purposes, generate random data
        data = self.create_candle_data(num_candles=140)
        data = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close'])

        # Convert datetime to float for x-axis
        data['Date'] = data['Date'].astype(int) / 10**9  # Convert to seconds

        # Plot candlestick chart
        candlesticks = pg.BarGraphItem(x=data['Date'], height=data['High'] - data['Low'],
                                       width=0.5, brush='w', pen='k')
        self.plot_widget.addItem(candlesticks)

        # Plot candlestick wicks
        wicks = pg.BarGraphItem(x=data['Date'], height=data['High'] - data['Close'],
                                width=0.2, brush='r', pen='r')
        self.plot_widget.addItem(wicks)

        wicks = pg.BarGraphItem(x=data['Date'], height=data['Open'] - data['Low'],
                                width=0.2, brush='g', pen='g')
        self.plot_widget.addItem(wicks)

        # Set labels and title
        self.plot_widget.setLabel('left', 'Price')
        self.plot_widget.setLabel('bottom', 'Date')
        self.plot_widget.setTitle('Cryptocurrency Price Chart')

    def create_candle_data(self, num_candles=30):
        # Initialize with random data for the first candle
        dates = pd.date_range(start='2022-01-01', periods=num_candles)
        ohlc = [(dates[0], 175, 180, 160, 175)]

        for i in range(1, num_candles):
            open_price = ohlc[-1][4]
            high_price = open_price + random.uniform(0, 10)
            low_price = open_price - random.uniform(0, 10)
            if low_price < 0:
                low_price = 0
            close_price = random.uniform(low_price, high_price)
            ohlc.append((dates[i], open_price, high_price, low_price, close_price))

        df = pd.DataFrame(ohlc, columns=['Date', 'Open', 'High', 'Low', 'Close'])
        df.set_index('Date', inplace=True)
        return df

