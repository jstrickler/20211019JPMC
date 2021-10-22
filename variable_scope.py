
x = 100  # global name

def spam():
    x = 1234  # don't do this
    y = 42  # local name
    print("in spam() x is", x)

spam()
# print("in main: y is", y)
print("in main: x is", x)

