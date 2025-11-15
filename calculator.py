"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    try:
        ans = a < 0
    except:
        print("ValueError")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b): 
    ans = a + b
    return ans


def sub(a,b):
    ans = a - b
    return ans

def mul(a,b):
    ans = a * b
    return ans

def div(a,b):
    try:
        ans = a/b
    except ZeroDivisionError:
        print("ZeroDivisionError")
    ans = a/b
    return ans

def log(a,b):
    try:
        ans = a > 0
        ans_2 = b > 0
    except ValueError:
        print("ValueError")

    ans = math.log(a,b)
    return ans

def pow(a,b):
    ans = a ** b
    return ans

