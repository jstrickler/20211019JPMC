d1 = dict()  # empty dict
state = 'AZ'
d2 = {state: 'Santa Fe', 'NC': 'Raleigh', 'WA': "Olympia"}
d3 = {}  # also empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['EWR'])
print(airports['RDU'])
code = 'LAX'
if code in airports:
    print(airports[code])
print()

print(airports.get('RDU'))
print(airports.get(code))
print(airports.get(code, 'NOT FOUND'))
print(airports.get('rdu', 'NOT FOUND BECAUSE CASE DID NOT MATCH'))
print(airports.get('WOMBAT', 123))

print(airports, '\n')
print(airports.setdefault('LAX', 'Los Angeles'))
print(airports, '\n')

more_airports = {'MIA': 'Miami', 'JAX': 'Jacksonville', 'TPA': 'Tampa',
                 'IAD': 'Dulles International'}

airports.update(more_airports)
print(airports, '\n')

airports['BOS'] = "Boston Logan"
airports['ORD']  = "Chicago"
print(airports, '\n')

for code, name in airports.items():
    print(code, name)
print()

print(airports.keys())
print(airports.values())

for code in airports:
    print(code)



