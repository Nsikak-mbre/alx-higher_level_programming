#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = 'Last digit of'
last_digit = number % 10
if last_digit > 5:
    print('{0} {1} is {2} and is greater than 5'.format(
        str1, number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print('{0} {1} is {2} and is less than 6 and not 0'.format(
        str1, number, last_digit))
elif last_digit == 0:
    print('{0} {1} is {2} and is 0'.format(str1, number, last_digit))
