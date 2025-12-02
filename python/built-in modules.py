#os
import os

print(os.name)  # Get the name of the OS
print(os.getcwd())  # Get current working directory
os.mkdir("example_folder")  # Create a new directory
os.rmdir("example_folder")  # Remove a directory

#Sys
import sys

print(sys.version)  # Get Python version
print(sys.path)  # List of module search paths


#math
import math
print(math.sqrt(16))  # Square root
print(math.pi)  # Pi value
print(math.factorial(5))  # Factorial

#Random
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice
print(random.shuffle([1, 2, 3, 4]))  # Shuffle list

#Datetime
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # Current datetime
print(now + timedelta(days=5))  # Add 5 days
print(now.strftime("%Y-%m-%d"))  # Format date

#json
import json
data = {"name": "John", "age": 30}
json_data = json.dumps(data)  # Convert to JSON string
print(json_data)
dict_data = json.loads(json_data)  # Convert back to dictionary
print(dict_data)

#Collections
from collections import Counter, namedtuple
  # Counter
fruits = ['apple', 'banana', 'apple']
print(Counter(fruits))
  # Namedtuple
Point = namedtuple("Point", "x y")
p = Point(10, 20)
print(p.x, p.y)

#re
import re
text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Match found:", match.group())

#Itertools
import itertools
for item in itertools.permutations([1, 2, 3], 2):
    print(item)

#functools
from functools import lru_cache
@lru_cache(maxsize=3)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

#Statistics
import statistics
data = [1, 2, 3, 4, 5]
print(statistics.mean(data))  # Mean
print(statistics.median(data))  # Median
