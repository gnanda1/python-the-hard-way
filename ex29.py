# What IF

# declare variables.

from lib2to3.pgen2.token import EQUAL


people = 20
cats = 30
dogs = 15

if people < cats: # 20 < 30
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs: # 20 < 15
    print("The wold is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5
print(f"Dogs: {dogs}")

if people >= dogs: # 20 >= 20
    print("People are greater than or equal to dogs.")

if people <= dogs: # 20 <= 20
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
