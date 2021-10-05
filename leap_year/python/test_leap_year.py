import pytest
from leap_year import leapYear

YEAR_START = 1900
YEAR_END = 2018

@pytest.mark.parametrize(
    'year',
    (i for i in range(YEAR_START, YEAR_END) if i % 4 != 0)
)
def test_that_a_year_not_divisible_by_4_is_not_a_leap_year(year):
    assert not leapYear(year)

@pytest.mark.parametrize(
    'year',
    (i for i in range(YEAR_START, YEAR_END) if i % 4 == 0 and i % 100 != 0)
)
def test_that_a_year_divisible_by_4_but_not_by_100_is_a_leap_year(year):
    assert leapYear(year)

@pytest.mark.parametrize(
    'year',
    (i for i in range(YEAR_START, YEAR_END) if i % 100 == 0 and i % 400 != 0)
)
def test_that_a_year_divisible_by_100_but_not_by_400_is_not_a_leap_year(year):
    assert not leapYear(year)

@pytest.mark.parametrize(
    'year',
    (i for i in range(YEAR_START, YEAR_END) if i % 400 == 0)
)
def test_that_a_year_divisible_by_400_is_a_leap_year(year):
    assert leapYear(year)

if __name__ == '__main__':
    pytest.main()