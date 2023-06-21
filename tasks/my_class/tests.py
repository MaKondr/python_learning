from Human import *
from SmallHouse import *


def main():
    Human.default_info()
    human = Human(
        'John',
        30
    )
    human.info()

    house = SmallHouse(price=6355150)
    human.buy_house(house=house, discount=10)

    for day in range(12 * 10):
        human.work(50000)

    human.buy_house(house=house, discount=10)

    human.info()


if '__main__' == __name__:
    main()
