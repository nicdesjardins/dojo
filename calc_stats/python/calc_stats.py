
class CalcStats(object):
    
    __INSTRUCTIONS__ = "Please provide an array of 2 or more numbers."
        
    def __init__(self, sequence = None):
        if sequence != None:
            self.set_sequence(sequence)
    
    def get_sequence(self):
        return self.__sequence__
    
    def set_sequence(self, sequence):
        newSequence = []
        
        if isinstance(sequence, list):
            for value in sequence:
                try:
                    newSequence.append(float(value))
                except Exception as ex:
                    raise Exception(self.__INSTRUCTIONS__)
            self.__sequence__ = newSequence
        else:
            raise Exception(self.__INSTRUCTIONS__)

    sequence = property(get_sequence, set_sequence)

    def max(self):
        return max(self.get_sequence())

    def min(self):
        return min(self.get_sequence())

    def sorted(self):
        return sorted(self.get_sequence())

    def length(self):
        return len(self.get_sequence())
    
    def average(self, arr = None):
        if arr == None:
            arr = self.get_sequence()
        return sum(arr) / len(arr)
    
    def median(self):
        if self.hasEvenNumberOfElements(self.get_sequence()):
            return self.average(
                self.middleElements(self.sorted())
            )
        else:
            return self.middleElement(sorted(self.get_sequence()))
    
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
    
    if len(arr) < 2:
        print("Please provide at least 2 numbers.")
        sys.exit(0)
    
    try:
        cs = CalcStats(arr)
        print("Sequence: ", str(cs.sequence))
        print("Sorted: ", cs.sorted())
        print("Minimum value: ", cs.min())
        print("Maximum value: ", cs.max())
        print("Number of elements in the sequence: ", cs.length())
        print("Average: ", cs.average())
        print("Median: ", cs.median())
    except Exception as ex:
        print(ex)