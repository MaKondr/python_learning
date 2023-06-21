from my_packages import cat
from my_packages.human.man import john
from mary import foo

def main():
    print(f'my name: {__name__}')
    foo()

if __name__ == '__main__':
    main()