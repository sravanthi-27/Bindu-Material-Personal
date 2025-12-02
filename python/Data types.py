#NUMERIC TYPES

x = 42
y = 3.14
z = 2 + 3j
print(x+y)   # Output : 45.14
print(type(x))   # Output : <class 'int'>
print(type(y))   # Output : <class 'float'>
print(type(z))   # Output : <class 'complex'>
# when we done the operation with complex numbers the outcome comes in ()
print(y+z)   # Output : (5.140000000000001+3j)
print(y-z)   # Output : (1.1400000000000001-3j)
print(y*z)   # Output : (6.28+9.42j)
print(x/z)   # Output : (6.461538461538462-9.692307692307693j)
#print(y//z)  error - unsupported type
#print(y%z)   error - unsupported type
print(y**z)   # Output : (-9.444862917508688-2.8295364690120692j)
print(y==z)   # Output : False
print(y!=z)   # Output : True
#print(y<z)  error - not supported between instances of float and complex
#print(y>z)  error - not supported between instances of float and complex
#print(y>=z)  error - not supported between instances of float and complex
#print(y<=z)  error - not supported between instances of float and complex

#SEQUENCE TYPES
s = "hello"
print(s)   # Output : hello
print(s[1:4])   # Output : ell
s = 'hello'
print(s)   # Output : hello
print(s[1:4])   # Output : ell
s = '''hello'''
print(s)   # Output : hello
print(s[1:4])   # Output : ell
print(type(s))   # Output : <class 'str'>

list1 = [1,2,3]
print(list1)   # Output : [1, 2, 3]
list1.append(4)
print(list1)   # Output : [1, 2, 3, 4]
print(type(list1))   # Output : <class 'list'>

tuple1 = (1,2,3)
print(tuple1)   # Output : (1, 2, 3)
print(type(tuple1))   # Output : <class 'tuple'>

#SET TYPES
set1 = {1,2,2,3}
print(set1)   # Output : {1, 2, 3}
set1.add(4)
print(set1)   # Output : {1, 2, 3, 3}
print(type(set1))   # Output : <class 'set'>

#MAPPING TYPE
dict1 = {"name":"Alice","age":25}
print(dict1)   # Output :{'name': 'Alice', 'age': 25}
dict1 = {'''name''':'''Alice''','''age''':25}
print(dict1)   # Output :{'name': 'Alice', 'age': 25}
dict1 = {'name':'Alice','age':25}
print(dict1)   # Output :{'name': 'Alice', 'age': 25}
print(dict1["name"])   # Output : Alice
print(type(dict1))   # Output : <class 'dict'>

#BINARY TYPES
ba = bytearray(b"hello")
print(ba)   # Output : bytearray(b'hello')
ba[0] = ord('H')
print(ba)   # Output : bytearray(b'Hello')
print(type(ba))   # Output : <class 'bytearray'>

#BOOLEAN TYPE
a = True
print(True and False)   # Output : False
print(type(a))   # Output : <class 'bool'>

#NONE TYPE
x = None
print(x)   # Output : None
print(x is None)   # Output : True
print(type(x))   # Output : <class 'NoneType'>