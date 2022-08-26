# Else and If

# declare variables

people = 30
cars = 40
trucks = 15

if cars > people: # 40 > 30
    print("We should take the cars.")
elif cars < people: # 40 < 30
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars: # 15 > 40 - False
    print("That's too many trucks.")
elif trucks < cars: # 15 < 40 - True
    print("May be we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks: # 30 > 15
    print("Alright, lets just take the trucks.")
else:
    print("Fine, let's stay home then.")

# trying complex bool expression with ifelse

if (people > trucks) or (trucks > cars):
    print("Complex Bool IF Statement")
else:
    print("End of the program.")

if (people > trucks) and (trucks > cars):
    print("Complex Bool IF Statement")
else:
    print("End of the program.")

