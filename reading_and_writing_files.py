import sys
file_name = sys.argv[1]   # get 1st cmd line arg

file_name = "DATA/mary.txt"

mary_in = open(file_name, "r")
mary_in.close()

with open(file_name) as mary_in:
    pass

with open(file_name) as mary_in:
    for raw_line in mary_in:   # mary_in is a *generator* of lines
        line = raw_line.rstrip()
        print(line)
print("-" * 60)

with open(file_name) as mary_in:
    contents = mary_in.read()  # read entire file into string
    print("normal:")
    print(contents)  # human friendly
    print("raw:")
    print(repr(contents))  # code friendly
print('-' * 60)


with open(file_name) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print()

with open(file_name) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print()

#  for raw_line in file_obj:
#     pass
# one_string = file_obj.read()    entire file as a string
# list_of_strings = file_obj.readlines() all lines with newlines
# list_of_strings = one_string.splitlines()  all lines without newlines

word_count = 0
s = "e"
with open('DATA/words.txt') as words_in:
    with open('results.txt', 'w') as results_out:
        for raw_line in words_in:
            line = raw_line.rstrip()
            if line.endswith(s):
                results_out.write(raw_line)
                word_count += 1
print(f"{word_count} words end with {s}")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')
