"""OBJECTS:
(1)  what is object
(2)  iterable objects and range
(3)  dictionary
(4)  error handlinG

"""

print("===== object =====")

import array
import math
from math import ceil

# An object has its STATE and METHOD propoerties
# attribute is feature of object
# In Python, everythiung is object !!!

print(type("Hello world"))
print(type(100))
print(type(True))
print(type(math))
print(type(array))


result1 = math.ceil(97.8)  # call
result2 = ceil(99.8)

print(f"result1 is {result1}")
print(f"result2 is {result2}")
