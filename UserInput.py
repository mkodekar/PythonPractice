from UnderstandingClasses import Calci as c

x = input('Please enter the firt number\n')
y = input('Please enter the second number\n')
z = input('what would you like to do\n')
name = input('What is your name ?\n')

if z == 'multiply':
    c.multiplication(x, y, name)
elif z == 'divide':
    c.divisition(x, y, name)
elif z == 'subtract':
    c.subtraction(x, y, name)
elif z == 'add':
    c.addition(x, y, name)
else:
    print("Operation not found")
