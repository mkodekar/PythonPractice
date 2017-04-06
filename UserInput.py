import UnderstandingClasses

x = input('Please enter the firt number\n')
y = input('Please enter the second number\n')
z = input('what would you like to do\n')
name = input('What is your name ?\n')

if z == 'multiply':
    UnderstandingClasses.Calci.multiplication(x, y, name)
elif z == 'divide':
    UnderstandingClasses.Calci.divisition(x, y, name)
elif z == 'subtract':
    UnderstandingClasses.Calci.subtraction(x, y, name)
elif z == 'add':
    UnderstandingClasses.Calci.addition(x, y, name)
else:
    print("Operation not found")
