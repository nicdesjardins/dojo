import re

class AddFractions(object):
    
    fractions = []

    def __init__(self, operation):
        self.operation = operation
        self.fractions = []
        self.parseOperation()

    def lowestFraction(self, fraction):
        num, div = fraction
        lowest_divider = i = 1

        while i <= num:
            if self.divisible(fraction, i):
                lowest_divider = i
            i += 1

        return [
            int(num / lowest_divider),
            int(div / lowest_divider)
        ]
    
    def divisible(self, fraction, i):
        num, div = fraction
        return (
            num % i == 0
            and div % i == 0
        )

    def parseOperation(self):
        self.fractions = []
        for match in self.operationToMatches():
            self.fractions.append(self.matchToFraction(match))
    
    def operationToMatches(self):
        return re.findall('[0-9]+/[0-9]+', self.operation)

    def matchToFraction(self, match):
        split = match.split('/')
        return [int(split[0]), int(split[1])]

class nFraction(object):

    def __init__(self, number, divisor):
        self.number = number
        self.divisor = divisor

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str(self.number) + "/" + str(self.divisor)

if __name__ == '__main__':
    nf = nFraction(1, 5)
    print(nf)