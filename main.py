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

    def getConstant(self, eq):
        i = 0
        const = ""
        inConst = False

        while i < len(eq):

            if eq[i - 1] == "=":
                inConst = True

            print("got here")

            if inConst:
                if eq[i] == " ":
                    const = const
                else:
                    const += eq[i]

            i += 1

        return const

    def getYCoefficient(self, eq):
        i = 0

        while i < len(eq):
            if eq[i] == "y":
                return eq[i - 1]

            i += 1

    def solveSystem(self):
        eq1 = self.generateEquation()
        eq2 = self.generateEquation()

        eq1XCo = self.getXCoefficient(eq1)
        eq1YCo = self.getYCoefficient(eq1)

        eq2XCo = self.getXCoefficient(eq2)
        eq2XCo = self.getYCoefficient(eq2)

        # 1️⃣ Step 1: Eliminate x
        eq1YCo = eq1YCo * eq2XCo

        eq1 = f"{eq1YCo}"
