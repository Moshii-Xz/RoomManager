from ctypes.wintypes import FLOAT


def IsValidName(name):
    return len(name) != 0 and name.isalpha()


def IsInteger(number):
    is_integer = None
    try:
        check_number = int(number)
        is_integer = True
    except:
        is_integer = False
    return is_integer

def IsDecimal(decimal_number):
    is_decimal = None
    try:
        check_number = float(decimal_number)
        is_decimal = True
    except:
        is_decimal = False
    return is_decimal

def IsLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
def IsPositive(number):
    return number >= 0
