#IMPLICIT TYPE CASTING
x = 10
y = 5.5
print("addition is:",x+y)

#EXPLICIT TYPE CASTING
#1.Integer to float
x = 5
y  = float(x)
print(y)
#2.Float to integer
x = 5.9
y = int(x)
print(y)
#3.String to integer
x = "123"
y = int(x)
print(y)
#4.string to float
x = "123.45"
y = float(x)
print(y)

'''int(): Converts a value to an integer.
float(): Converts a value to a float.
str(): Converts a value to a string.
list(): Converts a value to a list.
tuple(): Converts a value to a tuple.'''

# Convert character to ASCII value
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")
# Output: The ASCII value of 'A' is 65

# Convert ASCII value to character
ascii_value = 65
char = chr(ascii_value)
print(f"The character for ASCII value {ascii_value} is '{char}'")
# Output: The character for ASCII value 65 is 'A'
