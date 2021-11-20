import re
from tabulate import tabulate

class AddFractions(object):
    
    REGEX_FIND_FRACTIONS = '[0-9]+/[0-9]+'
    explain = True
    fractions = []
    operation = ''
    SECTION_WIDTH = 80

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

    def explainOperationToFractions(self):
        if not self.explain:
            return
        self.explainIt('\n------------------------')
        print("Found the following fractions:")
        self.printFractions()

    def printFractions(self):
        for fraction in self.fractions:
            print(self.fractionToString(fraction))
        return

    def findFractionsInOperation(self):
        return re.findall('[0-9]+/[0-9]+', self.operation)

    def stringToFraction(self, stringFraction):
        split = stringFraction.split('/')
        return [int(split[0]), int(split[1])]

    def denominatorize(self, denominator):
        if denominator == 2:
            return 'half'
        elif denominator == 3:
            return str(denominator)+'rd'
        elif denominator == 4:
            return 'quater'
        else:
            return str(denominator)+'th'

    def addFractions(self, operation = None):
        if operation != None:
            self.parseOperation(operation)
        lowestCommonDenominator = self.findLowestCommonDenominator()
        self.explainIt('Add them as '+self.denominatorize(lowestCommonDenominator)+'s:')
        result = [0, lowestCommonDenominator]
        for key, fraction in enumerate(self.fractions):
            if key != 0:
                self.explainIt('+')
            self.explainIt(self.fractionToString([self.amountOfDenominators(fraction, lowestCommonDenominator), lowestCommonDenominator])+' ('+self.fractionToString(fraction)+')')
            result[0] += self.amountOfDenominators(fraction, lowestCommonDenominator)
        
        stringFraction = self.fractionToString(result)
        stringFractionWithWholes = self.fractionToString(result, True)
        same = stringFraction == stringFractionWithWholes
        self.explainIt('=\n' + stringFraction + (' (or '+stringFractionWithWholes + ')' if not same else ''))
        self.explainIt('\n------------------------\n')

        return self.fractionToString(self.lowestFraction(result), True)
    
    def fractionToString(self, fraction, extractWholes = False):
        numerator, denominator = fraction
        
        if not extractWholes:
            return str(numerator)+"/"+str(denominator)
        
        if numerator >= denominator:
            remainder = numerator % denominator
            wholes = int((numerator - remainder) / denominator)
            return str(wholes)+(" & "+str(remainder)+"/"+str(denominator) if remainder > 0 else '')
        else:
            return str(numerator)+"/"+str(denominator)

    def amountOfDenominators(self, fraction, toDenominator):
        numerator, denominator = fraction
        multiplier = toDenominator / denominator
        return int(numerator * multiplier)

    def explainTitle(self):
        if self.explain:
            print("\n" + self.sideStars(">") + " " + self.title + " " + self.sideStars(">"))
    
    def explainIt(self, output):
        if self.explain:
            print(output)

    def findLowestCommonDenominator(self):
        # self.title = 'Find the lowest common denominator'
        # self.explainTitle()
        lowestCommonDenominator = 1
        for key, fraction in enumerate(self.fractions):
            denominator = fraction[1]
            if key == 0:
                lowestCommonDenominator = denominator
                # self.explainIt('If we\'re on the first fraction, take it as the lowest common denominator')
                # self.explainIt('lcd = '+str(lowestCommonDenominator))
            else:
                if denominator != lowestCommonDenominator:
                    # self.explainIt('If the denominator for this fraction isn\' the same as the lowest common denominator, multiply the two and take that as the lowest common denominator.')
                    # self.explainIt('Denominator: '+str(denominator))
                    # self.explainIt('New lcd = '+str(denominator * lowestCommonDenominator)+' ('+str(denominator)+' * '+str(lowestCommonDenominator)+')')
                    lowestCommonDenominator = denominator * lowestCommonDenominator
        self.explainIt('\nFound the lowest common denominator: '+str(lowestCommonDenominator)+'\n')
        # self.explainIt(self.repeatStr("<", self.SECTION_WIDTH + 2))
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