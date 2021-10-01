
class CalcStats(object):
    def __init__(self, sequence):
        self.calcStats(sequence)

    def sum(self, arr):
        sum = 0
        for v in arr:
            sum += v
        return sum
    
    def avg(self, arr):
        return self.sum(arr) / len(arr)

    def median(self, arr):
        sorted_arr = sorted(arr)
        if len(sorted_arr) % 2 == 0:
            median = self.avg(
                [
                    sorted_arr[int((len(sorted_arr)/2)-1)],
                    sorted_arr[int((len(sorted_arr)/2))]
                ]
            )
        else:
            median = sorted_arr[
                int(
                    (
                        len(sorted_arr)-1
                    ) / 2
                )
            ]
        
        return median


    def calcStats(self, sequence):
        print("Sequence: ", sequence)
        print("Sorted: ", sorted(sequence))
        print("Minimum value: ", min(sequence))
        print("Maximum value: ", max(sequence))
        print("Number of elements in the sequence: ", len(sequence))
        print("Average: ", self.avg(sequence))
        print("Median: ", self.median(sequence))

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