import math

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return rectangle_area(side, side)

