from test_classes import *


def main():
    my_animal = Dog(say="Whow!", color='white',
                    names='sharik', )
    show(my_animal)


def show_info(animal):
    for i in animal.info_animal().items():
        print(f'{i[0]}: {i[1]}')
        yield i


def show(animals):
    i = 0
    a = show_info(animals)
    print("Input 'n' to continue: ")
    while i != 3:
        my_input = input()
        if my_input == 'n':
            next(a)
            i += 1
        else:
            print('Incorrect input, try again')


if "__main__" == __name__:
    main()
