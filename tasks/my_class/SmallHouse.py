from House import *


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(area=SmallHouse.default_area, price=price)
