import money

class Dollar(money.Money):
    def __init__(self, amount, currency='USD'):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
