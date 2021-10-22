food_counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        if food in food_counts:  # key exists
            food_counts[food] += 1  # increment value
        else:  # key does not exist
            food_counts[food] = 1   # add key

print(food_counts)
for food, count in food_counts.items():
    print("{:>18s} {:2d}".format(food, count))