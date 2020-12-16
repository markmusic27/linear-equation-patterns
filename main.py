from random import randint


class LinearEquationPattern:
    def __init__(self, minNum, maxNum):
        self.minNum = minNum,
        self.maxNum = maxNum,

    def generateEquation(self):
        xCoefficient = randint(self.minNum[0], self.maxNum[0])
        yCoefficient = randint(self.minNum[0], self.maxNum[0])
        interval = yCoefficient - xCoefficient
        constant = yCoefficient + interval
        return f"{xCoefficient}x + {yCoefficient}y = {constant}"

    def getXCoefficient(self, eq):
        i = 0

        while i < len(eq):
            if eq[i] == "x":
                return eq[i - 1]

            i += 1

    def getYCoefficient(self, eq):
        i = 0

        while i < len(eq):
            if eq[i] == "y":
                return eq[i - 1]

            i += 1

    def solveSystem(self):
        eq1 = self.generateEquation()
        eq2 = self.generateEquation()
