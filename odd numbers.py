# print odd numbers up to number 139
from random import random


def odd_number(item):
    return item % 2 == 0


if __name__ == "__main__":
    lst = [1, 2, 4, 4, 2, 3, 52, 3, 5, 23, 432, 5, 321, 5, 3, 123, 1234, 53,
           32, 253, 123, 432, 121, 139, 33, 4125, 436, 643]
    for i in lst:
        if odd_number(i):
            print(i)
        if i == 139:
            print("now 139")
            break
