#Defining functions
def my_function():
    print("Hello world")
my_function()

#Function Arguments
def greet(name):
    print("hello",name)
greet("Bindu")

#Return statements
def add(a,b):
    return a+b
result = add(2,4)
print(result)

#Lambda functions
multiply = lambda x,y: x*y
print(multiply(3,4))

#Recursive functions
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n*factorial(n-1)
print(factorial(6))

#Higher-order functions
def apply_func(f,x):
    return f(x)
def square(n):
    return n*n
result = apply_func(square , 5)
print(result)

#Default arguments
def greet(name = "Default"):
    print("hello",name)
greet()
greet("Bindu")

#Variable-length arguments   (*args)
def print_all(*args):
    for arg in args:
        print(arg)
print_all(1,"a",2)
#                            (**kwargs)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
display_info(name="alice",age=30,city="newyork")

#kwargs providing default behaviour
def greet_user(**kwargs):
    greeting = kwargs.get("greeting", "Hello")
    name = kwargs.get("name", "Guest")
    print(greeting, name)
greet_user(greeting="Hi", name="Alice")
greet_user(name="bob")
greet_user(greeting="Hey")

#Passing kwargs to another function
def add_person_to_database(**kwargs):
    print("Adding person with details")
    print_details(**kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
add_person_to_database(name="john",age=30,occupation="engineer")

#Using kwargs with other parameters
def display_profile(username, **kwargs):
    print(f"Username: {username}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_profile("john_doe",age=28, city="san francisco",hobbies=["reading","cycling"])

#User defined functions
  #Fruitful functions
def add_numbers(a, b):
    return a + b
# Calling the function
result = add_numbers(5, 3)
print("Result:", result)  # Output: Result: 8

  #Non fruitful function
def print_message(name):
    print(f"Hello, {name}!")
# Calling the function
print_message("Alice")  # Output: Hello, Alice!
# Assigning the result of the function to a variable
result = print_message("Alice")
print(result)  # Output: None
