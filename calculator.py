# https://github.com/rylieeaton/lab10-RE-YT  
# Partner 1: Rylie Eaton
# Partner 2: Yasmin Tatari

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both base and argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b
