import math
import typing as T

def get_message():
    return "Hello, JPMC world"

print(get_message)  # function object

print(get_message())  # function return value
result = get_message()
print("result is", result)

def say_hello():
    message = get_message()
    print(message)
    # return None    (implied)

say_hello()

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius ** 2)

print(circle_area(1))
print(circle_area(2))
print(circle_area(42))
print(circle_area(123.456))

Number = T.Union[int, float]


def rectangle_area(length: Number, width: Number) -> Number:
    return length * width

print(rectangle_area(5, 10))
print(rectangle_area(8, 23.3983))
print(rectangle_area(5, "foo"))

#         pos........  named.......
#         req     opt
def wacky(p1, p2, *p3, p4, p5, **p6):
    pass


def config(**data):
    print(data)

config(file_name="wombats.txt", user_name="silly_sam", country="Burkina Faso")

a = 10
b = 48.9
print(a, b, end=' ')
print()

# like the 'real' print() function
def my_print(*args, end='\n', sep=' '):
    pass


