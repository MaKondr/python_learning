

class House:

    def __init__(self, *, price=None, area=None):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * ((100 - discount) / 100)
