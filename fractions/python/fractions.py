import re
from tabulate import tabulate

class AddFractions(object):
    
    REGEX_FIND_FRACTIONS = '[0-9]+/[0-9]+'
    explain = True
    fractions = []
    operation = ''
    def __init__(self, operation, explain = None):
        self.fractions = []
        self.operation = operation
        self.parseOperation(operation)
        if explain != None:
            self.explain = explain

    def parseOperation(self, operation=None):
        if operation != None:
            self.operation = operation
        
        self.operationToFractions()
        self.explainOperationToFractions()
    
    def operationToFractions(self):
        self.clearFractions()
        for stringFraction in self.findFractionsInOperation():
            self.appendFractionToFractions(
                self.stringToFraction(stringFraction)
            )

    def clearFractions(self):
        self.fractions = []

    def appendFractionToFractions(self, fraction):
        self.fractions.append(fraction)

    SECTION_WIDTH = 80

    title = ''
    def explainOperationToFractions(self):
        if self.explain:
            self.title = "Explain Operation to Fractions"
            titleLength = len(self.title)
            
            print("\n" + self.sideStars(">") + " " + self.title + " " + self.sideStars(">"))
            print("operation = '"+self.operation+"'")
            print("matches = re.findall('"+self.REGEX_FIND_FRACTIONS+"', operation)")
            print("Found the following fractions:")
            self.printFractions()
            print(self.repeatStr("<", self.SECTION_WIDTH + 2)+"\n")

    def sideStars(self, char):
        titleLength = len(self.title)
        numSideStars = int((self.SECTION_WIDTH - titleLength) / 2)
        return self.repeatStr(char, numSideStars)

    def repeatStr(self, string, length):
        out = ''
        for i in range(1, length):
            out += string
        return out

    def printFractions(self):
        # for fraction in self.fractions:
        #     print(str(fraction[0]) + "/" + str(fraction[1]))
        table = []
        row = 0
        for fraction in self.fractions:
            row += 1
            table.append({'row': row, 'fraction': str(fraction[0]) + "/" + str(fraction[1])})
        print(tabulate(table, headers="keys"))


    def findFractionsInOperation(self):
        return re.findall('[0-9]+/[0-9]+', self.operation)

    def stringToFraction(self, stringFraction):
        split = stringFraction.split('/')
        return [int(split[0]), int(split[1])]

    def addFractions(self, operation = None):
        if operation != None:
            self.parseOperation(operation)
        lowestCommonDenominator = self.findLowestCommonDenominator()
        result = [0, lowestCommonDenominator]
        for key, fraction in enumerate(self.fractions):
            result[0] += self.amountOfDenominators(fraction, lowestCommonDenominator)

        return self.fractionToString(self.lowestFraction(result))
    
    def fractionToString(self, fraction):
        numerator, denominator = fraction
        if numerator >= denominator:
            remainder = numerator % denominator
            wholes = int((numerator - remainder) / denominator)
            return str(wholes)+" & "+str(remainder)+"/"+str(denominator)
        else:
            return str(numerator)+"/"+str(denominator)

    def amountOfDenominators(self, fraction, toDenominator):
        numerator, denominator = fraction
        multiplier = toDenominator / denominator
        return int(numerator * multiplier)

    def findLowestCommonDenominator(self):
        lowestCommonDenominator = 1
        for key, fraction in enumerate(self.fractions):
            denominator = fraction[1]
            if key == 0:
                lowestCommonDenominator = denominator
            else:
                if denominator != lowestCommonDenominator:
                    lowestCommonDenominator = denominator * lowestCommonDenominator
        return lowestCommonDenominator

    def lowestFraction(self, fraction):
        numerator, denominator = fraction
        lowest_divider = i = 1

        while i <= numerator:
            if self.divisible(fraction, i):
                lowest_divider = i
            i += 1

        return [
            int(numerator / lowest_divider),
            int(denominator / lowest_divider)
        ]
    
    def divisible(self, fraction, i):
        num, div = fraction
        return (
            num % i == 0
            and div % i == 0
        )

class Fract(object):
    def __init__(self, number, denominator):
        self.number=number
        self.denominator=denominator
    
    def __str__(self):
        return str(self.number)+"/"+str(self.denominator)

import sys
if __name__ == "__main__":
    operation = ''
    for key, arg in enumerate(sys.argv):
        if key > 0:
            operation += arg
    
    af = AddFractions(operation)
    print(af.addFractions())