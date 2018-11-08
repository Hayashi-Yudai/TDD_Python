import money

class Franc(money.Money):
    def __init__(self, amount, currency='CHF'):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
