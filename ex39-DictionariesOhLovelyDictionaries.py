# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Massachusetts': 'MA',
    'Nevada': 'NV'
    }

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'MA': 'Boston',
    'NV': 'Las Vegas'
    }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

#### Testing what else I can do
# Set a key to a value
cities['MA'] = 'Cambridge'
print(cities['MA'], '\n')

# Delete a key from a dictionary
del cities['MA']
print(cities, '\n')

# Print boolean if Key in dictionary
print('MA' in cities, '\n')
# Print boolean if Key not in dictionary
print('MA' not in cities, '\n')

# iterate through all the keys in cities.
for keys in iter(cities):
    print(keys)

# clear all items from the dictionary
cities.clear()
print(cities, '\n')

# add cities back 
cities['CA'] = 'San Francisco'
cities['MI'] = 'Detroit'
cities['FL'] = 'Jacksonville'
cities['MA'] = 'Boston'
cities['NV'] = 'Las Vegas'
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print(cities, '\n')

# Shallow copy of the dicitionary to a new dictionary
new_cities = cities.copy()
print(new_cities, '\n')

# Create a new dictionary with keys from seq and values.
seq = ('rivers', 'captial', 'temp')

new_cities = dict.fromkeys(seq)
print(f'{new_cities}','\n')

# return the value of a key if in the dictionary or the default None
print(cities.get('CA', 'None'))
print(cities.get('AZ', 'None'), '\n')

# returns a new view of a dictionary tuple pairs (key, value)
print('Cities : ', cities.items(), '\n')

# Reutrns a list of all available keys in the dictionary
print('States :', states.keys(), '\n')

# Remove a key from the dictionary if found otherwise return an error or the default supplied.
print(cities.pop('NV', 'None'))
print(cities, '\n')

# Remove and return a key value pair from the dicionary. LIFO Order. 
print(cities.popitem(), '\n')

# if a key is in the dictionary return its value or set the value of the key to default.
print(cities.setdefault('AL', 'None'))
print(cities)

# Update/Adds the dictionary with key value pairs from other (another dictionary or iterable tuples)
