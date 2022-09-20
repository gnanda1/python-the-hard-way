# import modules 
from add import add_func # another way to call our module 
import sub
import multiply
import division

print("Welcome to Python Calculator. Select any choice from below.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division.")

prompt = input("> ")

x = int(input("Enter first integer: "))
y = int(input("Enter second integer: ")) 

if prompt == '1':
    add_func(x, y)
elif prompt == '2':
    sub.sub_func(x, y)
elif prompt == '3':
    multiply.multiply_func(x, y)
elif prompt == '4':
    division.division_func(x, y)
else: 
    print("End the Program. Try again....")