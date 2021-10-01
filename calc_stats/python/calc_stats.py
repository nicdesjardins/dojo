
class CalcStats(object):
    def __init__(self, sequence = []):
        self.sequence = sequence
        self.calcStats()

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


    def calcStats(self):
        print("Sequence: ", self.sequence)
        print("Minimum value: ", min(self.sequence))
        print("Maximum value: ", max(self.sequence))
        print("Number of elements in the sequence: ", len(self.sequence))
        print("Average: ", self.avg(self.sequence))
        print("Median: ", self.median(self.sequence))


if __name__ == "__main__":
    CalcStats([6, 9, 15, -2, 92, 11, 100])