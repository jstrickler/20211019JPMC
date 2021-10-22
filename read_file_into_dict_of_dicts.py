from pprint import pprint  # import pprint function from pprint module

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

pprint(knight_info)
print()

print(knight_info['Galahad']['color'], '\n')

#   key   value
for name, data in knight_info.items():
    print(data['title'], name)
print()
