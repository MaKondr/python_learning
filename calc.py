# calc

def calc(a, b, operation):
    if operation == 1:
        print('Sum ' + str(a + b))
        return a + b
    elif operation == 2:
        print('Subtraction ' + str(a - b))
        return a - b
    elif operation == 3:
        print('Multiplication ' + str(a * b))
        return a * b
    elif operation == 4:
        print('Division ' + str(int(a / b)))
        return int(a / b)


calc(515, 15, 4)
