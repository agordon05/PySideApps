class exchange:

    def __init__(self, status: str, exchange1: str, name: str, usdt: float, profit: float):
        self.status = status
        self.exchange = exchange1
        self.name = name
        self.usdt = usdt
        self.profit = profit

    def button_click(self):
        print(f"button clicked: {self.name}")
