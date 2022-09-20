"""
A file containing a set of functions you want to include in your application.
A module can define functions, classes, and variables. 
A module can also include runnable code. 
Grouping related code into a module makes the code easier to understand and use.
It also makes the code logically organized.
"""

from stock import *


print("Select any option from below: ")
print("1. Apple")
print("2. Tesla")
print("3. Coca Cola")

prompt = input("> ") 

if prompt == "1":
    print(apple_stock())

if prompt == "2":
    print(tesla_stock())

if prompt == "3":
    print(coke_stock())


# print all dict

print(apple)
print(tesla)
print(coke)