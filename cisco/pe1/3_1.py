"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 1 Making decisions in Python
"""
# two is two
print(2 == 2)

# integer two is widened to float and compared against float two
print(2 == 2.0)


def lab_3_1_6(n):
    """print False if n is less than 100, and True if n is greater than or equal to 100"""
    print(n >= 100)


lab_3_1_6(55)

# Conditional execution: the if statement
sheep_counter = 222
if sheep_counter >= 120:
    print('I feel sleepy')

# The if-else statement: more conditional execution
if sheep_counter >= 320:
    print('I feel sleepy')
else:
    print('Let see some more sheep')


def lab_3_1_10(name):
    """
    parameter
        name: a flower name

    return
        "Yes - Spathiphyllum is the best plant ever!" for name Spathiphyllum

        "No, I want a big Spathiphyllum!" for name spathiphyllum

        "Spathiphyllum! Not [input]!" for other [input]    
    """
    if name == 'Spathiphyllum':
        print('Yes - Spathiphyllum is the best plant ever!')
    elif name == 'spathiphyllum':
        print('No, I want a big Spathiphyllum!')
    else:
        print('Spathiphyllum! Not', name + '!')


lab_3_1_10('Amaryllis')


def lab_3_1_11(income):
    """
    Personal Income Tax calculator

    parameter:
        income, a personal income
    return:
        the calculated tax, rounded to full thalers

    if income is higher than 85_528, PIT is 14_839.2 plus 32% of the surplus over 85,528 thalers.
    Otherwise is 18% of income minus 556.2 (tax relief)
    """
    PIT_LIMIT = 85_528.0
    PIT_BASE_AMOUNT = 14_839.2
    PIT_HIGH_PCT = 0.32
    PIT_LOW_PCT = 0.18
    PIT_RELIEF = 556.2

    if income > PIT_LIMIT:
        result = PIT_BASE_AMOUNT + PIT_HIGH_PCT * (income - PIT_LIMIT)
    else:
        result = income * PIT_LOW_PCT - PIT_RELIEF
        if result < 0:
            result = 0

    return round(result)

print('Checking taxes')
print(lab_3_1_11(10_000) == 1_244)
print(lab_3_1_11(100_000) == 19_470)
print(lab_3_1_11(1_000) == 0)
print(lab_3_1_11(-100) == 0)


def lab_3_1_12(year):
    """
    Leap Year detector

    parameter:
        year, a year
    return:
        "Leap year", "Common year", or "Not within the Gregorian calendar period" if year < 1582
    """
    if year < 1582:
        return 'Not within the Gregorian calendar period'
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 'Leap year'
    else:
        return 'Common year'

print('Checking leap years')
print(lab_3_1_12(2_000) == 'Leap year')
print(lab_3_1_12(1_900) == 'Common year')
print(lab_3_1_12(2_015) == 'Common year')
print(lab_3_1_12(1_999) == 'Common year')
print(lab_3_1_12(1_996) == 'Leap year')
print(lab_3_1_12(1_580) == 'Not within the Gregorian calendar period')
