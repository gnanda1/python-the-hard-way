## Asking Questions

print("How old are you ?", end=' ')
age = input()
print("How tall are you ?", end=" ")
height = input()
print("How much do you weight?", end=' ')
weight = input()

#print(f"So, you're age is {age}, old, {height} tall and {weight} heavy.")
# Another way to format above print statement.
print("So, your age is {} old, {} tall and {} heavy.".format(age, height, weight))

print(type(age))
print(type(height))
print(type(weight))