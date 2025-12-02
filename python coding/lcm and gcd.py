from functools import reduce
import math
# Function to find GCD of a list
def find_gcd(arr):
    return reduce(math.gcd, arr)  # Computes GCD for multiple numbers

# Function to find LCM of two numbers
def find_lcm(x, y):
    return (x * y) // math.gcd(x, y)  # Formula for LCM

# Function to find LCM of a list
def lcm_of_array(arr):
    return reduce(find_lcm, arr)  # Applies LCM iteratively

# Input lists
a = [2, 6]
b = [24,36]

# Compute LCM of a and GCD of b
lcm_a = lcm_of_array(a)
gcd_b = find_gcd(b)
