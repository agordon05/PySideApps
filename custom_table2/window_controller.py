import sys
from PySide6 import QtWidgets
import main_window
from custom_table import Custom_Table

app = QtWidgets.QApplication()
# window = main_window.Main_Window()
table_widget: Custom_Table = Custom_Table()


def update_table(data=None):
    if data is None:
        table_widget.refresh_data()
    else:
        table_widget.update_data(data)


def new_table(table: Custom_Table):
    global table_widget
    table_widget = table


def run_ui():
    window = main_window.Main_Window()
    # window.setFixedSize(1000, 600)
    window.setWindowTitle("Custom Table 2")
    window.show()

    sys.exit(app.exec())
