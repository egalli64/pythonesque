"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 4 Section 3 – Returning a result from a function
"""
# return without an expression


def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


happy_new_year()
happy_new_year(False)

# return with an expression


def boring_function():
    return 123


x = boring_function()
print("The boring_function has returned its result. It's:", x)


def boring_function_2():
    print("'Boredom Mode' ON.")
    return 123


print("This lesson is interesting!")
# returned value could be ignored
boring_function_2()
print("This lesson is boring...")

# 4.3.2 A few words about None
useless = None
print("useless is", useless)
try:
    print(useless + 2)
except TypeError:
    print("'None' can be only assigned or compared with")

if useless is None:
    print("This variable is not really useful")


def strange_function(n):
    """If n is even None is implicitly returned"""
    if (n % 2 == 0):
        return True


print(strange_function(2))
print(strange_function(1))

# 4.3.3 Effects and results: lists and functions


def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s


print("List sum:", list_sum([5, 4, 3]))
try:
    list_sum(42)
except TypeError:
    print("Unexpected argument type!")


def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list


print("Calling a list generator:", strange_list_fun(5))

# 4.3.4 LAB - leap year


def is_year_leap(year):
    if year < 1582:
        return False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# 4.3.5 LAB - How many days


def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    delta = 1 if month == 2 and is_year_leap(year) else 0
    return days[month - 1] + delta


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# 4.3.6 LAB - Day of the year


def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        days += days_in_month(year, m)
    if day >= 1 and day <= days_in_month(year, month):
        return days + day
    else:
        return None


print(day_of_year(2000, 12, 31))
print(day_of_year(1900, 12, 31))

# 4.3.7 LAB - Prime numbers


def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True


for i in range(2, 21):
    if is_prime(i):
        print(i, end=" ")
print()

# 4.3.8 LAB - Converting fuel consumption
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

MILE = 1609.344
GALLON = 3.785411784


def liters_100km_to_miles_gallon(litres):
    return (100 * 1000 / MILE) / (litres / GALLON)


def miles_gallon_to_liters_100km(miles):
    return GALLON / (miles * MILE / 1000 / 100)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
