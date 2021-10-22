import sqlite3

try:
    file_name = "DATA/wombats.txt"
    with open(file_name) as file_in:
        pass
except FileNotFoundError as err:
    print(err)

data = [1, 5, 19, 47]
try:
    print(data[12])
except IndexError as err:
    print(err, type(err))


number = 23
for value in 5, 8, 0, 12, 19:
    try:
        result = number / value
    except ZeroDivisionError as err:
        print(err)
    else:  # no exceptions raised
        print(result)


conn = None
try:
    with sqlite3.connect('foo/bar/blah.db') as conn:
        cursor = conn.cursor()
        cursor.execute('select * from wombats')
        for row in cursor.fetchall():
            print(row)
except sqlite3.OperationalError as err:
    print(err)
    exit()  # exit program
finally:
    if conn is not None:
        conn.close()

print("Done.")