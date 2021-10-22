# from pkg.pkg import module
# from john/math load geom.py
from john.math import geom, calculus
import sys

area = geom.circle_area(14)
print("area is", area)
print(geom.circle_area(1000))

print(geom.rectangle_area(18, 36))
print(geom.square_area(99))

# 1. current folder
# 2. folders in PYTHONPATH
# 3. predefined (python installation) folders


for path in sys.path:
    print(path)

