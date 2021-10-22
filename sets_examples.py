colors1 = 'red blue red red green orange yellow purple lilac'.split()
colors2 = 'green green lilac green brown black blue white orange'.split()
empty = set()  # empty set
c1 = set(colors1)
c2 = set(colors2)
c1.add('pink')
c2.add('magenta')
print("c1:", c1, '\n')
print("c2:", c2, '\n')

print("common:", c1 & c2)  # intersection
print("not common:", c1 ^ c2)  # xor
print("both:", c1 | c2)   # union
print("just c1:", c1 - c2)
print("just c2:", c2 - c1)
print()

for color in 'red', 'purple', 'navy', 'ecru', 'white', 'pink':
    print(color, color in c1, color in c2)
print()