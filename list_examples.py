list1 = list()   # empty list
list2 = [5, 6, 7, 8]
list3 = ['apple', 'banana', 'kiwi', 'mango', 'mangosteen']
list4 = []  # empty list

cities = ['Tokyo', 'Atlanta', 'Columbus', 'Durham', 'Houston']
print(cities[0], len(cities), cities[len(cities)-1])
print(cities[-1], cities[-2])  # same as cities[len(cities)-1]
cities[3] = 'Raleigh'
print(cities)
print(cities[-2])

list5 = 'apple banana kiwi'.split()
print(list5)

record = "spam:ham:eggs:toast"
fields = record.split(':')
print(fields, fields[0], fields[2], fields[-1], '\n')

print(cities)
cities.append('Mumbai')
cities.append('Paris')
cities.append('Edinburgh')
print(cities)
cities.insert(0, "Berlin")
cities.insert(3, "Madrid")
print(cities)
more_cities = ['Sebastopol', 'Lisbon', 'Casablanca']
cities.extend(more_cities)
print(cities)

# LIST.append(obj) LIST.insert(pos, obj) LIST.extend(iterable)
del cities[3]  # remove 4th element
print(cities)
c = cities.pop()
print(c)
print(cities)
c = cities.pop()  # -1
print(c)
print(cities)
c = cities.pop(1)
print(c, cities)
print(cities.pop(-2))
print(cities)

cities.remove('Mumbai')
print(cities)

#
#   LIST.insert(0, value)   push on left end
#   LIST.pop(0) pop from left end
#   LIST.append(value)  push on right end
#   LIST.pop()  pop from right end
cities[3] = "Durham"
print(cities)
# cities.replace('Raleigh', 'Durham')  NO NO NO
# x = cities.pop()

#  del LIST[pos]     LIST.pop(pos=-1)     LIST.remove(value)
print(cities[0], cities[4], cities[-1])

print(cities[0:3])  # slice     start:stop
print(cities[3:5])
print(cities[:4])
print(cities[5:])
print(cities[-3:])  # last 3 items
#    0         1
#    0123456789012345
s = "J P Morgan Chase"
print(s[4:10], s[-5:], s[11:], s[:3])

#  []  lookup operator
#  (xxx) precedence
#  thing()   call a thing

#  for VAR ... in ITERABLE:
#      ....

print()
for city in cities:  #  similar to foreach in other languages
    # city = next element of cities
    print(city)
print()

for color in 'red purple yellow orange black'.split():
    print(color.upper())
print()

s = 'abc'
#
for letter in s:
    print(letter)
print('\n')  # outputs '\n\n'




