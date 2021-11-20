import pytest
import datetime

from .leapyear import leapyear

LOWER_LIMIT = 1900
UPPER_LIMIT = 2021

@pytest.mark.parametrize('n, result',(i, leapyear(i)) for i in range(LOWER_LIMIT, UPPER_LIMIT) if i % 4 == 0)
def test__A_year_divisible_by_4_is_a_leapyear(n, result):
    assert leapyear(n) == True

@pytest.mark.parametrize('n, result',(i, leapyear(i)) for i in range(LOWER_LIMIT, UPPER_LIMIT) if i % 100 == 0 and i % 400 !=0)
def test__A_year_divisible_by_100_is_not_a_leap_year_unless_it_is_also_divisible_by_400(n, result):
    assert leapyear(n) == False

@pytest.mark.parametrize('n, result', (i, leapyear(i)) for i in range(LOWER_LIMIT, UPPER_LIMIT) if i % 100 == 0 and i % 400 == 0)
def test_A_year_divisible_by_100_and_divisible_by_400_is_a_leap_year(n, result):
    assert leapyear(n) == True

@pytest.mark.parametrize('n, result',(i, leapyear(i)) for i in range(LOWER_LIMIT, UPPER_LIMIT) if i % 400 == 0)
def test__A_year_divisible_by_400_is_a_leap_year(n, result):
    assert leapyear(n) == True
