
DEFAULT_LIMIT = 100

class FizzBuzz(object):

    def __init__(self):
        self.buffer = ''
        self.count = 0
        self.limit = None

    multiples = {
        3: 'Fizz',
        5: 'Buzz',
        7: 'Whizz',
        11: 'Bang',
        13: 'Booh!',
    }

    def isMultipleOf(self, multiple):
        return self.count % multiple == 0

    def run(self, limit = DEFAULT_LIMIT):
        self.limit = limit

        while not self.limitReached() and not self.hitSuperCombo():
            self.count += 1
            self.buffer = ''

            for multiple, say in self.multiples.items():
                if self.isMultipleOf(multiple):
                    self.buffer += say

            print(self.buffer or self.count)
    
    def limitReached(self):
        if self.limit != None:
            if self.count >= self.limit:
                return True
        return False
    
    def hitSuperCombo(self):
        return self.buffer == ''.join(self.multiples.values())
    

import sys

if __name__ == "__main__":
    limit = DEFAULT_LIMIT
    if len(sys.argv) > 1:
        if sys.argv[1].isnumeric():
            limit = int(sys.argv[1])
        elif sys.argv[1] == 'nolimit':
            limit = None
        else:
            print('Please provide an integer limit.')
            sys.exit(0)
    
    fb = FizzBuzz()
    fb.run(limit)
    
