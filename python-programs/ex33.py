# While Loops: A while-loop will keep executing the code block under it as long as a boolean expressioin is True.

# Declare variables.

i = 0
numbers = []

def while_loop():
    global i # declaring as global to use outside of the function.
    i = 0
    global numbers # declaring as global to use outside of the function.
    numbers = []
    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)
            
        i += 1 # or i = i + 1
            
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


while_loop()
print("The numbers: ")
for num in numbers:
    print(num)