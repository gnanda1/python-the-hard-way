# Dictionaries, Oh Lovely Dictionaries.
# create a map of state to abbreviation.

from os import stat


states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Virginia': 'VA',
    'Maryland': 'MD',
}

# Loop through the states
print("\nUS States and Abbreviations.")
for s, k in states.items():
    print(s,' \t ',k)

# Create a basic set of states and some cities in them.

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'VA': 'Richmond',
    'TX': 'Dallas',
    'MD': 'Baltimore'
}

# add some more cities.
cities['NY'] = 'Manhattan'
cities['OR'] = 'Portland'

# Loop through cities.
print("\nCities in USA")
for c, k in cities.items():
    print(c, ' \t ', k)

# print out some cities
print('-' * 15)
print("\n")
print("NY state has: ", cities['NY'])
print('OR state has: ', cities['OR'])

# print out some states.
print('-' * 15)
print("\n")
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
print("NewYork's abbreviation is:  ", states['New York'])

# do it by using the state than cities dict
print('-' * 15)
print("\n")
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
print("NewYork has: ", cities[states['New York']])


# print every state abbreviaton
print('-' * 15)
print("\n")
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev} ")

# print every city in state
print('-' * 15)
print("\n")
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time.
print('-' * 15)
print("\n")

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 15)
print("\n")
# safely get abbreviation by state that might not be there.
state = states.get('Illinois')

if not state:
    print('Sorry, no Illinois.')

# get a city with a default value.
city = cities.get('IL', 'Does Not Exist')
print(f"The city for the state 'IL' is: {city}")