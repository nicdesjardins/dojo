import re

class AddFractions(object):
    
    fractions = []

    def __init__(self, operation):
        self.fractions = []
        self.parseOperation(operation)

    def parseOperation(self, operation=None):
        if operation != None:
            self.operation = operation
        self.fractions = []
        for stringFraction in self.operationToMatches():
            self.fractions.append(self.stringToFraction(stringFraction))
    
    def operationToMatches(self):
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
            if remainder > 0:
                return str(wholes)+ " & " + str(remainder)+"/"+str(denominator)
            else:
                return wholes
            
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