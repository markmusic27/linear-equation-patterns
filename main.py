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

        print("Original Equations:")
        print(eq1)
        print(eq2)

        eq1XCo = int(self.getXCoefficient(eq1))
        eq1YCo = int(self.getYCoefficient(eq1))
        eq1Const = int(self.getConstant(eq1))

        eq2XCo = int(self.getXCoefficient(eq2))
        eq2YCo = int(self.getYCoefficient(eq2))
        eq2Const = int(self.getConstant(eq2))

        eq1 = f"-1({eq1XCo}) + 2({eq1YCo}) = {eq1Const}"
        eq2 = f"-1({eq2XCo}) + 2({eq2YCo}) = {eq2Const}"

        print("")
        print("Plug-In Variables:")
        print(eq1)
        print(eq2)


obj = LinearEquationPattern(1, 9)

obj.solveSystem()
