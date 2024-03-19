#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
addition = add(a, b)
print('{} + {} = {}'.format(a, b, addition))

subtract = sub(a, b)
print('{} + {} = {}'.format(a, b, subtract))

divide = div(a, b)
print('{} + {} = {}'.format(a, b, divide))

multiply = mul(a, b)
print('{} + {} = {}'.format(a, b, multiply))

if __name__ == "__main__":
    add(a, b)
    sub(a, b)
    div(a, b)
    mul(a, b)
