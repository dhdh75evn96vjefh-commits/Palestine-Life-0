class EconomySystem:
    def __init__(self):
        self.currency = "دينار"
    def process_payment(self, amount):
        return f"تمت المعالجة: {amount} {self.currency}"

