
actor = "Chris Hemsworth"
print(type(actor), len(actor))

print(actor.upper())
x = actor.upper()

#  FUNC(obj)    obj.METHOD()
print(actor.count('h'))
print(actor.lower().count('h'))  # method chaining
print(actor.startswith('Chris'))
print(actor.startswith(('Fred', 'Chris', 'Liam')))
print(actor.startswith('Liam'), '\n')


print(actor.find('worth'))
print(actor.index('worth'))
print(actor.find('Liam'), '\n')

s1 = "        All my exes live in Texas         "   # probably Houston
print("|" + s1.lstrip() + "|")  # strip ' ' \t \n \r
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")  # lstrip + rstrip
print()

s2 = "xyxxxyyyxyxyyyyyyyAll my exes live in Texasxxxyyyxyxyxxxxxxx"
print("|" + s2.lstrip("xy") + "|")  # strip 'x' OR 'y'
print("|" + s2.rstrip("xy") + "|")
print("|" + s2.strip("xy") + "|")  # lstrip + rstrip
print()

fruit_data = "mango:durian:mangosteen:kiwi"
fruits = fruit_data.split(':')
print(fruits)

names = "Billy Srini Lakshmi Yi Wanda Vision".split()
print(names)
print("/".join(names))
print(";".join(fruits))
print(sorted(names))
print(" + ".join(sorted(names)))
print("\n".join(names))










