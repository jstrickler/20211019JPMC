a = "Fred Flintstone"
b = "Bedrock"
c = 23.30293093

print()    # print('\n')
print(a)   #  print(str(a) + '\n')
print(a, b)  # print(str(a) + ' ' + str(b) + '\n')
print(a, b, c, sep=" *** ")
print(a, b, sep="/")
print(a)
print(b)
print(c)
print(a, end=' ')
print(b, end=' ')
print(c)
print(a, b, c, sep=' ', end='\n')  # defaults
print()

print(a, "lives in", b)
print("{} lives in {}".format(a, b))
print("Value is {:.3f}".format(c))
count = 23
print("Count is {:04d}".format(count))
print("Count is {:4d}".format(count))
big_number = 2358203958203958203523555731313456
print("Large number: {:,d}".format(big_number))
print(f"{a} lives in {b}")  # f string   f-string  3.6 and later
print(f"Value is {c:.3f}")
print(f"Count is {count:04d}")




