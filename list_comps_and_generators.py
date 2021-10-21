fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

#  [EXPR for VAR in ITERABLE]
#  [EXPR for VAR in ITERABLE if CONDITION]
f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

f4 = [f for f in fruits if f.startswith('p') and len(f) > 5]
print("f4:", f4, '\n')

f5 = [f for f in fruits if f.startswith('p') or len(f) > 8]
print("f5:", f5, '\n')

all_foods = ['spam', 'spam', 'broth', 'spam', 'spam', 'spam', 'spam',
             'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam',
             'spam', 'spam', 'toast', 'spam', 'spam', 'spam', 'spam',
             'spam', 'spam', 'naan', 'spam', 'spam', 'spam', 'eggs']

foods = [f for f in all_foods if f != 'spam']
print('foods:', foods, '\n')

# tuple
# x = (obj, obj, obj, obj, ...)

foods_gen = (f for f in all_foods if f != 'spam')
for food in foods_gen:
    print(food.upper())
print()
print(foods_gen)

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

dob_list = [p[3] for p in people]
print(dob_list)
dob_gen = (p[3] for p in people)
print(dob_gen)
for dob in dob_gen:
    print(dob)
print('-' * 60)
for dob in dob_gen:
    print(dob)
print(dob_gen)
