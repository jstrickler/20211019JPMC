fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

nums = [800,80,1000,32,255,400,5,5000]

print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits), '\n')

print(len(nums), min(nums), max(nums), sum(nums))
print(sorted(nums), '\n')

rnums = reversed(nums)
for num in rnums:
    print(num, end=' ')
print('\n')
print(rnums)

rnums = reversed(nums)
print(type(rnums))

# can't do:
# print(len(rnums))
# print(rnums[0])

fruits = fruits[:10]
print(fruits)
for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
print(list(enumerate(fruits)))

print('boo' * 10)
print([True] * 5)
x = [None] * 100
print(x)

print('-' * 60)

print("foo" + "bar")
print([1, 2, 3] + [4, 5, 6])




