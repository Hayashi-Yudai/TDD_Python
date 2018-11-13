class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
    
    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')