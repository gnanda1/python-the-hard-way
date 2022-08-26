# Accessing elements of a list.

animals = ['bear', 'tiger', 'penguin', 'zebra']
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])

num = 0
for animal in animals:
    print(f"At index {num}:  ", animal)
    num = num + 1

print(animals)
