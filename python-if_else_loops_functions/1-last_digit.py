#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    l_digit = number % 10
elif number < 0:
    l_digit = ((number * -1) % 10) * -1
print(f"Last digit of {number} is", end=" ")
if (l_digit < 6 and l_digit != 0):
    print(f"{l_digit} and is less than 6 and not 0")
elif (l_digit > 5):
    print(f"{l_digit} and is greater than 5")
else:
    print(f"{l_digit} and is 0")
