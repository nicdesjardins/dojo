
def fizzbuzz(n):
    return {
        (False, False): str,
        (True, False): lambda _: 'Fizz',
        (False, True): lambda _: 'Buzz',
        (True, True): lambda _: 'FizzBuzz'
    }[(n % 3 == 0, n % 5 == 0)](n)

import sys
if __name__ == '__main__':
    if len(sys.argv) == 2:
        n = sys.argv[1]
        if n.isnumeric():
            print(fizzbuzz(int(n)))
            exit(0)
    print('Please provide a single integer.')