from collections import namedtuple

a1 = 1, 2, 3    # tuple
a2 = [1, 2, 3]  # list
a3 = {1, 3, 2}  # set

person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(person, len(person))
print(person[0], person[1])

first_name = person[0]
last_name = person[1]
# ...

#  list of variables  =  iterable_object
first_name, last_name, product, dob = person   # unpack iterable to vars
print(first_name, last_name)

a = 45
b = 6
print(a // b, a % b)
print(divmod(a, b))

x, y = divmod(a, b)
print(x)
print(y)

result = divmod(a, b)
print(result[0], result[1])

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
print(people[0])
print(people[0][0])
print(people[0][0][0])

for person in people:
    print(person[0], person[1], person[2])
print()

for first_name, last_name, product, dob in people:
    print(first_name, last_name, product)
print()

if people[0][3] < people[1][3]:
    print("younger")

#  named tuples
#  dataclasses

Person = namedtuple('Person', 'first_name last_name product dob')
data = []
for row in people:
    person = Person(row[0], row[1], row[2], row[3])
    person = Person(*row)
    data.append(person)

print(data[0].first_name, data[0].dob)
print(data[0][0], data[0][3])
print()
for person in data:
    print(person.first_name, person.last_name)


colors = [
    'purple',
    'yellow',
    'red',
    'blue',
]
