
x = 5    #  x = int(x)   create int object, bind name 'x'
y = 10

result = x + y
print(result)

# a-z A-Z 0-9 _

# GOOD: customer_number  primary_source_file
#  BAD  cnum   CustomerNumber
#  REALLY BAD: pri_SOURCE_filE

customer_id = None   # null-ish

current_class = "Junior"

compass_direction = "north"

cd = compass_direction

print(type(x), type(compass_direction), type(cd))

a = "123"
b = 456
# print(a + b)

print(type(a), type(b))

this_is_a_ridiculously_long_variable_name_that_I_would_never_really_use = "wombat"
print(this_is_a_ridiculously_long_variable_name_that_I_would_never_really_use)

# google: python type hints
def spam(p1: int, p2: int) -> int:  # test with mypy
    print(p1 + p2)

spam(10, 20)
spam('foo', 'bar')






