for i in range(5):
    print(i)
print()

#  range(STOP)   range(START, STOP)  range(START, STOP, STEP)

for i in range(1, 6):
    print(i, end=' ')
print('\n')

for i in range(5, 101, 5):
    print(i, end=', ' if i < 100 else '')
print('\n')