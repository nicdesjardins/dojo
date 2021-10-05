# Source of tests: Kevlin Henney's talk: Structure and interpretatio of test cases
import pytest
from fb import fizzbuzz

UPPER_LIMIT = 101

@pytest.mark.parametrize(
    'n, result', 
    ((i, fizzbuzz(i)) for i in range(1, UPPER_LIMIT))
)
def test_that_every_result_is_Fizz_Buzz_FizzBuzz_or_decimal(n, result):
    assert result in {'Fizz', 'Buzz', 'FizzBuzz'} or result.isdecimal()

@pytest.mark.parametrize(
    'n, result',
    ((i, fizzbuzz(i)) for i in range(1, UPPER_LIMIT) if fizzbuzz(i).isdecimal())
)
def test_that_every_decimal_result_corresponds_to_its_input(n, result):
    assert int(result) == n

@pytest.mark.parametrize('n', range(3, UPPER_LIMIT, 3))
def test_that_every_third_result_contains_Fizz(n):
    assert 'Fizz' in fizzbuzz(n)

@pytest.mark.parametrize('n', range(5, UPPER_LIMIT, 5))
def test_that_every_fifth_result_contains_Buzz(n):
    assert 'Buzz' in fizzbuzz(n)

@pytest.mark.parametrize('n', range(15, UPPER_LIMIT, 15))
def test_that_every_fifteenth_result_is_FizzBuzz(n):
    assert fizzbuzz(n) == 'FizzBuzz'

@pytest.mark.parametrize(
    'n',
    (i for i in range(1, UPPER_LIMIT) if fizzbuzz(i) == 'Fizz')
)
def test_that_the_input_for_every_Fizz_is_divisible_by_3(n):
    assert n % 3 == 0

@pytest.mark.parametrize(
    'n',
    (i for i in range(1, UPPER_LIMIT) if fizzbuzz(i) == 'Buzz')
)
def test_that_the_input_for_every_Buzz_is_divisible_by_5(n):
    assert n % 5 == 0

@pytest.mark.parametrize(
    'n',
    (i for i in range(1, UPPER_LIMIT) if fizzbuzz(i) == 'FizzBuzz')
)
def test_that_the_input_for_every_FizzBuzz_is_divisible_by_15(n):
    assert n % 15 == 0

if __name__ == '__main__':
    pytest.main()