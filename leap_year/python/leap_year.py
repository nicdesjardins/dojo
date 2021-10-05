
def leapYear(year):
    # a year divisible by 100 and not by 400 is not a leap year
    if year % 100 == 0 and year % 400 != 0:
        return False
    # a year divisible by 4 is a leap year
    elif year % 4 == 0:
        return True
    # a year divisible by 400 is a leap year
    elif year % 400 == 0:
        return True
    # a year not divisible by 4 is not a leap year
    else:
        return False
