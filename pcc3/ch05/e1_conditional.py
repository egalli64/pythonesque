"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 5 -If Statement - Conditional Tests
"""
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# assignment vs comparison
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

# inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# numeric comparison
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

print(answer < 21)
print(answer <= 21)
print(answer > 21)
print(answer >= 21)

print(answer < 21 and car == 'bmw')
print(answer > 21 or car == 'bmw')

print('Is bmw in list?', 'bmw' in cars)

other_car = 'alfa'
if other_car not in cars:
    print(f"{other_car.title()} not available")

game_active = True
if game_active:
    print('Game is active')