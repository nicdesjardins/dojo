
class CalcStats(object):
    def __init__(self, sequence):
        self.calcStats(sequence)
    
    def calcStats(self, sequence):
        print("Sequence: ", sequence)
        print("Sorted: ", sorted(sequence))
        print("Minimum value: ", min(sequence))
        print("Maximum value: ", max(sequence))
        print("Number of elements in the sequence: ", len(sequence))
        print("Average: ", self.avg(sequence))
        print("Median: ", self.median(sequence))
    
    def avg(self, arr):
        return sum(arr) / len(arr)
    
    def median(self, arr):
        sorted_arr = sorted(arr)
        if self.hasEvenNumberOfElements(sorted_arr):
            return self.avg(
                self.middleElements(sorted_arr)
            )
        else:
            return self.middleElement(sorted_arr)
    
    def hasEvenNumberOfElements(self, arr):
        return len(arr) % 2 == 0

    def middleElement(self, arr):
        return arr[int((len(arr)-1) / 2)]
    
    def middleElements(self, arr):
        return [
            arr[int((len(arr)/2)-1)],
            arr[int((len(arr)/2))]
        ]

import sys
if __name__ == "__main__":
    arr = []
    for key, arg in enumerate(sys.argv):
        if key > 0:
            try:
                value = float(arg)
                arr.append(value)
            except ValueError:
                print("Please provide a list of numbers only.")
                sys.exit(0)
    
    if len(arr) == 0:
        print("Please provide at least 2 numbers.")
        sys.exit(0)
    
    CalcStats(arr)