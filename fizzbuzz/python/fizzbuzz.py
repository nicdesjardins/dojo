
DEFAULT_LIMIT = 100

class FizzBuzz(object):

    def __init__(self):
        self.buffer = ''
        self.count = 0
        self.limit = None

    multiples = {
        3: 'Fizz',
        5: 'Buzz',
        # 7: 'Whizz',
        # 11: 'Bang',
        # 13: 'Booh!',
    }

    def isMultipleOf(self, n, multiple):
        return n % multiple == 0

    def fb(self, n):
        self.buffer = ''
        for multiple, say in self.multiples.items():
            if self.isMultipleOf(n, multiple):
                self.buffer += say
        return self.buffer or str(n)

    def run(self, limit = DEFAULT_LIMIT):
        self.limit = limit

        while not self.limitReached() and not self.hitSuperCombo():
            self.count += 1
            print(self.fb(self.count))
    
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
    
