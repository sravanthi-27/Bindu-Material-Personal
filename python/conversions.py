#INTEGER
x = 32
print("INTEGER CONVERSIONS:")
print(int(x))
print(float(x))
print(str(x))
print(bool(x))
#print(list(x))   TypeError: 'int' object is not iterable
#print(tuple(x))  TypeError: 'int' object is not iterable
#print(set(x))    TypeError: 'int' object is not iterable
#print(dict(x))   TypeError: 'int' object is not iterable
print(bytes(x))
print(bytearray(x))
#print(memoryview(x))   TypeError: memoryview: a bytes-like object is required, not 'int'

#FLOAT
y = 3.14
print("FLOAT CONVERSIONS:")
print(int(y))
print(float(y))
print(str(y))
print(bool(y))
#print(list(y))   TypeError: 'float' object is not iterable 
#print(tuple(y))  TypeError: 'float' object is not iterable
#print(set(y))    TypeError: 'float' object is not iterable
#print(dict(y))   TypeError: 'float' object is not iterable
#print(bytes(y))  TypeError: cannot convert 'float' object to bytes
#print(bytearray(y))   TypeError: cannot convert 'float' object to bytearray
#print(memoryview(y))   TypeError: memoryview: a bytes-like object is required, not 'float'

#COMPLEX
z = 3+4j
print("COMPLEX CONVERSIONS:")
#print(int(z))          TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(float(z))        TypeError: float() argument must be a string or a real number, not 'complex'
print(str(z))
print(bool(z))
#print(list(z))         TypeError: 'complex' object is not iterable
#print(tuple(z))        TypeError: 'complex' object is not iterable
#print(set(z))          TypeError: 'complex' object is not iterable
#print(dict(z))         TypeError: 'complex' object is not iterable
#print(bytes(z))        TypeError: cannot convert 'complex' object to bytes
#print(bytearray(z))    TypeError: cannot convert 'complex' object to bytearray
#print(memoryview(z))   TypeError: memoryview: a bytes-like object is required, not 'complex'

#STRING
a="bindu"
print("STRING CONVERSIONS:")
#print(int(a))            ValueError: invalid literal for int() with base 10: 'bindu'
#print(float(a))          ValueError: could not convert string to float: 'bindu'
print(str(a))
print(bool(a))
print(list(a))   
print(tuple(a))  
print(set(a))    
#print(dict(a))           ValueError: dictionary update sequence element #0 has length 1; 2 is required
#print(bytes(a))          TypeError: string argument without an encoding
#print(bytearray(a))      TypeError: string argument without an encoding
#print(memoryview(a))     TypeError: memoryview: a bytes-like object is required, not 'str'

#BOOLEAN
a = True
print("BOOLEAN CONVERSIONS:")
print(int(a))
print(float(a))
print(str(a))
print(bool(a))
#print(list(a))             TypeError: 'bool' object is not iterable
#print(tuple(a))            TypeError: 'bool' object is not iterable
#print(set(a))              TypeError: 'bool' object is not iterable  
#print(dict(a))             TypeError: 'bool' object is not iterable
print(bytes(a))
print(bytearray(a))
#print(memoryview(a))       TypeError: memoryview: a bytes-like object is required, not 'bool'

#LIST
l = ["a",1]
print("LIST CONVERSIONS:")
#print(int(l))              TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#print(float(l))            TypeError: float() argument must be a string or a real number, not 'list'
print(str(l))
print(bool(l))
print(list(l))   
print(tuple(l))  
print(set(l))    
#print(dict(l))             ValueError: dictionary update sequence element #0 has length 1; 2 is required
#print(bytes(l))            TypeError: 'str' object cannot be interpreted as an integer
#print(bytearray(l))        TypeError: 'str' object cannot be interpreted as an integer
#print(memoryview(l))       TypeError: memoryview: a bytes-like object is required, not 'list'

#TUPLE
t = ("a",1)
print("TUPLE CONVERSIONS:")
#print(int(t))               TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
#print(float(t))             TypeError: float() argument must be a string or a real number, not 'tuple'
print(str(t))
print(bool(t))
print(list(t))   
print(tuple(t))  
print(set(t))    
#print(dict(t))               ValueError: dictionary update sequence element #0 has length 1; 2 is required
#print(bytes(t))              TypeError: 'str' object cannot be interpreted as an integer
#print(bytearray(t))          TypeError: 'str' object cannot be interpreted as an integer
#print(memoryview(t))         TypeError: memoryview: a bytes-like object is required, not 'tuple'

#SET
s = {"b",1,"a"}
print("SET CONVERSIONS:")
#print(int(s))                TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
#print(float(s))              TypeError: float() argument must be a string or a real number, not 'set'
print(str(s))
print(bool(s))
print(list(s))   
print(tuple(s))  
print(set(s))    
#print(dict(s))                 TypeError: cannot convert dictionary update sequence element #0 to a sequence
#print(bytes(s))                TypeError: 'str' object cannot be interpreted as an integer
#print(bytearray(s))            TypeError: 'str' object cannot be interpreted as an integer
#print(memoryview(s))           TypeError: memoryview: a bytes-like object is required, not 'set'

#DICTIONARY
d = {"age":13,"Name":"bindu","weight":10}
print("DICTIONARY CONVERSIONS:")
#print(int(d))                  TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
#print(float(d))                TypeError: float() argument must be a string or a real number, not 'dict'
#print(str(d))                  TypeError: 'str' object cannot be interpreted as an integer
print(bool(d))
print(list(d))   
print(tuple(d))  
print(set(d))    
print(dict(d))   
#print(bytes(d))                TypeError: 'str' object cannot be interpreted as an integer
#print(bytearray(d))            TypeError: 'str' object cannot be interpreted as an integer
#print(memoryview(d))           TypeError: memoryview: a bytes-like object is required, not 'dict'