class Calci:
    def addition(self, other, name):
        added = int(self) + int(other)
        print(name, 'your answer is ', added)

    def subtraction(self, other, name):
        subtracted = int(self) - int(other)
        print(name, 'your answer is ', subtracted)

    def multiplication(self, other, name):
        multiplication = int(self) * int(other)
        print(name, 'your answer is', multiplication)

    def divisition(self, other, name):
        divide = int(self) / int(other)
        print(name, 'your answer is ', divide)


if __name__ == '__main__':
    print()
## For output see Importing2.py
