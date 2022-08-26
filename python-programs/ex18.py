## Names, Variables, Code, Functions.

"""
Functions do three things.
    * They name pieces of code the way variables name strings and numbers.
    * They take arguments the way your scripts take argv
    * Using 1 and 2, they let you make your own "mini-scripts" or "tiny commands".
"""

# this function is like your scripts with argv
# def for "define"

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this function just takes one argument.
def print_one(arg1):
    print(f"arg1: {arg1}")

# this function takes no arguments.
def print_none():
    print("I got nothi'.")


# Calling functions.
print_two("Jurassic", "Park")
print_two_again("Jurassic", "World")
print_one("First!")
print_none()