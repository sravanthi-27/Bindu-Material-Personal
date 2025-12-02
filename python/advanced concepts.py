#Decorator
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello, World!")

say_hello()
# Output:
# Before the function call
# Hello, World!
# After the function call

#Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
# Output:
# 5
# 4
# 3
# 2
# 1

#Extras: RIP
  #(a) Reduce
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
  #(b) Itertools
from itertools import combinations
items = ['a', 'b', 'c']
comb = combinations(items, 2)
print(list(comb))  # Output: [('a', 'b'), ('a', 'c'), ('b', 'c')]
  #(c) Partial 
from functools import partial
def multiply(x, y):
    return x * y
double = partial(multiply, y=2)
print(double(5))  # Output: 10

#refular expressions(regex)
import re

# Text to work with
text = "The rain in Spain stays mainly in the plain."

# 1. findall(): Returns all matches as a list
pattern = r'\b[a-z]{4}\b'  # Words with exactly 4 letters
words = re.findall(pattern, text)
print("findall():", words)  # Output: ['rain', 'main', 'plain']

# 2. search(): Finds the first match and returns a Match object
match = re.search(r'rain', text)
if match:
    print("search():", match.group())  # Output: rain

# 3. match(): Matches the pattern at the start of the string
match = re.match(r'The', text)
if match:
    print("match():", match.group())  # Output: The

# 4. split(): Splits the string by occurrences of the pattern
split_text = re.split(r'\s', text)  # Splits by whitespace
print("split():", split_text)  # Output: ['The', 'rain', 'in', 'Spain', ...]

# 5. sub(): Replaces all matches with a string
replaced_text = re.sub(r'rain', 'snow', text)
print("sub():", replaced_text)  # Output: The snow in Spain stays mainly in the plain.

# 6. subn(): Replaces all matches and returns a tuple (new string, number of replacements)
replaced_text, count = re.subn(r'in', 'out', text)
print("subn():", replaced_text)  # Output: The rout out Spout stays maoutly out the plout.
print("subn() count:", count)  # Output: 6

# 7. compile(): Pre-compiles a regex pattern for repeated use
compiled_pattern = re.compile(r'\b[a-z]{4}\b')
compiled_words = compiled_pattern.findall(text)
print("compile() with findall():", compiled_words)  # Output: ['rain', 'main', 'plain']

# 8. fullmatch(): Checks if the entire string matches the pattern
full_match = re.fullmatch(r'The rain in Spain', text)
print("fullmatch():", full_match)  # Output: None (because the entire string does not match)

# 9. finditer(): Returns an iterator of Match objects
iter_matches = re.finditer(r'\bin\b', text)
print("finditer():", [match.group() for match in iter_matches])  # Output: ['in', 'in', 'in']

# 10. escape(): Escapes special characters in a string for safe regex matching
special_text = "a+b*c?"
escaped_pattern = re.escape(special_text)
print("escape():", escaped_pattern)  # Output: a\+b\*c\?
