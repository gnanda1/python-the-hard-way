"""
- A Class is a blue print for how something should be defined.
- Attributes = is/has Ex: name, age, height
- method = actions Ex: eat, sleep, make youtube videos.

"""

class Person:
    "This is a Person Class"
    age = 10 # attribute

# method
    def greet(self):
        print("Hello")

print(Person.age)
print(Person.greet)
print(Person.__doc__)