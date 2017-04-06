def addition(num1, num2):
    print(num1 + num2)


def subtract(num1, num2):
    print(num1 - num2)


def multiply(num1, num2):
    print(num1 * num2)


def division(num1, num2):
    print(num2 / num1)


def modulus(num1, num2):
    print(num1 % num2)


def withDefParam(num1, num2=4):
    print(num1 + num2)
    print(num2 - num1)
    print(num2 * num1)


addition(2, 3)
subtract(5, 3)
multiply(9, 3)
division(3, 9)
modulus(9, 3)
withDefParam(9)
