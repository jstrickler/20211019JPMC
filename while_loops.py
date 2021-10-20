i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("Enter your name (or q to quit): ")
    if name == 'q':
        print("goodbye!")
        break  # exit loop
    if name == '':
        print("Please enter a name")
        continue
    print("Hello,", name)
