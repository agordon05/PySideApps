import sys
import random
from decimal import Decimal

import numpy as np
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import mplfinance as mpf


class StockChartWidget(QWidget):

    def __init__(self, buy_intervals: list[float] = None, sell_intervals: list[float] = None,
                 gen_intervals: list[float] = None):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.figure = Figure(facecolor='#282C34')  # Set the background color to a dark color
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.ax = self.figure.add_subplot(111)  # Use add_subplot to get the existing ax
        self.ax.set_facecolor('#282C34')  # Set the background color of the Axes

        self.create_stock_chart(buy_intervals=buy_intervals, sell_intervals=sell_intervals, gen_intervals=gen_intervals)

    def create_stock_chart(self, buy_intervals: list[Decimal] = None, sell_intervals: list[Decimal] = None,
                           gen_intervals: list[Decimal] = None):
        # No need to create a new figure and ax here
        self.update_stock_chart(buy_intervals=buy_intervals, sell_intervals=sell_intervals,
                                gen_intervals=gen_intervals)

    # Inside the update_stock_chart method
    def update_stock_chart(self, buy_intervals: list[Decimal] = None, sell_intervals: list[Decimal] = None,
                           gen_intervals: list[Decimal] = None):
        # Clear the existing plot
        self.ax.clear()

        # Set text and edge colors
        self.ax.set_title('Cryptocurrency Price Chart', color='white')
        self.ax.set_xlabel('Date', color='white')
        self.ax.set_ylabel('Price', color='white')

        # Set tick labels color
        for tick in self.ax.get_xticklabels() + self.ax.get_yticklabels():
            tick.set_color('white')

        # For demonstration purposes, generate random data
        data = self.create_candle_data(num_candles=140)
        data = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close'])

        # Plot candlestick chart
        mpf.plot(data, type='candle', mav=20, tight_layout=True, style='yahoo', ax=self.ax)

        self.create_trade_markers(buy_intervals=buy_intervals, sell_intervals=sell_intervals,
                                  gen_intervals=gen_intervals)

        # Adjust the width of the plot area
        self.figure.autofmt_xdate()
        self.figure.tight_layout()

        # Draw the canvas
        self.canvas.draw()

    def create_candle_data(self, num_candles=30):
        # Initialize with random data for the first candle
        dates = pd.date_range(start='2022-01-01', periods=num_candles)
        # ohl -- data, open, high, low, close
        ohlc = [(dates[0], 160, 180, 160,
                 175)]

        for i in range(1, num_candles):
            # Use the previous closing price as the open price for the current candle
            open_price = ohlc[-1][4]

            # Generate random values for high, low, and close
            high_price = open_price + random.uniform(0, 10)
            low_price = open_price - random.uniform(0, 10)

            if low_price < 0:
                low_price = 0

            close_price = random.uniform(low_price, high_price)

            # Append the new candlestick data to the list
            ohlc.append((dates[i], open_price, high_price, low_price, close_price))

        df = pd.DataFrame(ohlc, columns=['Date', 'Open', 'High', 'Low', 'Close'])
        df.set_index('Date', inplace=True)  # Set 'Date' column as the index

        return df

    def create_trade_markers(self, buy_intervals: list[float] = None, sell_intervals: list[float] = None,
                             gen_intervals: list[float] = None):

        # Plot colored horizontal lines for buy prices
        if not buy_intervals:
            buy_intervals = [140, 145, 150]
        for interval in buy_intervals:
            self.ax.axhline(interval, color='green', linestyle='-', linewidth=0.8, alpha=0.8, label='Buy Interval')

        # Plot colored horizontal lines for sell prices
        if not sell_intervals:
            sell_intervals = [175, 180, 190]
        for interval in sell_intervals:
            self.ax.axhline(interval, color='red', linestyle='-', linewidth=0.8, alpha=0.8, label='Sell Interval')

        # Plot colored horizontal lines for generic prices
        if not gen_intervals:
            gen_intervals = [160, 165, 170]
        for interval in gen_intervals:
            self.ax.axhline(interval, color='lightblue', linestyle='-', linewidth=0.8, alpha=0.8, label='Gen Interval')

        # Calculate the overall y-axis limits based on your intervals
        min_y_value = min(min(buy_intervals), min(sell_intervals), min(gen_intervals)) - 20
        max_y_value = max(max(buy_intervals), max(sell_intervals), max(gen_intervals)) + 20

        # Set the y-axis limits
        self.ax.set_ylim(bottom=min_y_value, top=max_y_value)