a = 10
b = 20

# ARITHMETIC OPERATORS
print("Arithmetic Operators:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division (returns float)
print("a % b =", a % b)   # Modulus (remainder)
print("a ** b =", a ** b) # Exponentiation (a to the power of b)
print("a // b =", a // b) # Floor Division (integer result)

# COMPARISON OPERATORS
print("\nComparison Operators:")
print("a == b:", a == b)   # Equal to
print("a != b:", a != b)   # Not equal to
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to

# LOGICAL OPERATORS
print("\nLogical Operators:")
x = 5
y = 10
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT

# BITWISE OPERATORS
print("\nBitwise Operators:")
print("a & b:", a & b)    # Bitwise AND
print("a | b:", a | b)    # Bitwise OR
print("a ^ b:", a ^ b)    # Bitwise XOR
print("~a:", ~a)          # Bitwise NOT
print("a << 2:", a << 2)  # Left shift
print("a >> 2:", a >> 2)  # Right shift

# ASSIGNMENT OPERATORS
print("\nAssignment Operators:")
c = a
print("c = a:", c)      # Assign value
c += b                  #c = c+b
print("c += b:", c)     # Add and assign
c -= b
print("c -= b:", c)     # Subtract and assign
c *= b
print("c *= b:", c)     # Multiply and assign
c /= b
print("c /= b:", c)     # Divide and assign
c %= b
print("c %= b:", c)     # Modulus and assign
c **= 2
print("c **= 2:", c)    # Exponentiation and assign
c //= b
print("c //= b:", c)    # Floor Division and assign

# MEMBERSHIP OPERATORS
print("\nMembership Operators:")
list1 = [1, 2, 3, 4, 5]
print("2 in list1:", 2 in list1)         # Check if 2 is in list1
print("6 not in list1:", 6 not in list1) # Check if 6 is not in list1

# IDENTITY OPERATORS
print("\nIdentity Operators:")
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("x is y:", x is y)     # False because x and y are different objects
print("x is z:", x is z)     # True because z references the same object as x
print("x is not y:", x is not y) # True because x and y are not the same object

# TERNARY OPERATOR
print("\nTernary Operator:")
max_value = a if a > b else b
print("Max value between a and b:", max_value)

# Operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

#Compare two boxes
class Box:
    def __init__(self, volume):
        self.volume = volume

    # Overload the < operator
    def __lt__(self, other):
        return self.volume < other.volume

# Create two boxes
box1 = Box(100)
box2 = Box(150)

# Compare the boxes
print(box1 < box2)  # Output: True (100 < 150)
print(box2 < box1)  # Output: False (150 is not less than 100)
