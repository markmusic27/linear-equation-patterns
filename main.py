from random import randint


def generateEquation(minNum, maxNum):
    xCoefficient = randint(minNum, maxNum)
    yCoefficient = randint(minNum, maxNum)
    interval = yCoefficient - xCoefficient
    constant = yCoefficient + interval
    print(f"{xCoefficient}x + {yCoefficient}y = {constant}")


generateEquation(0, 100)
