class Human:
    __default_name = "Bob"
    __default_age = 25

    def __init__(self, name=__default_name, age=__default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'name: {self.name}\n'
              f'age: {self.age}\n'
              f'money: {self.__money}\n'
              f'house: {self.__house}')

    @staticmethod
    def default_info():
        print(f'name: {Human.__default_name}\n'
              f'age: {Human.__default_age}')

    def work(self, earn):
        self.__money += earn
        print(f"Earned {earn} money! Current value: {self.__money}")

    def make_deal(self, *, price, house):
        if self.__house:
            print(f'{self.__default_name} bought a new house for {price}')
            self.__house = house
            self.__money -= price
        else:
            print(f'{self.__default_name} bought a first house for {price}')
            self.__house = house
            self.__money -= price

    def buy_house(self, *, house, discount):
        if self.__money < house.final_price(discount=discount):
            print(f"insufficient funds in the account\n"
                  f"you have: {self.__money}\n"
                  f"you need: {house.final_price(discount=discount) - self.__money}")
        else:
            print(f"You can buy this house!\n"
                  f"balance after purchase: {self.__money - house.final_price(discount=discount)}")
            print('\nMake deal?(Y/N)')
            if input() == 'Y':
                self.make_deal(house=house, price=house.final_price(discount=discount))
                print('Deal purchased!')
            else:
                print('Deal canceled!')
