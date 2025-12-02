#Class and Object
# Define a class
class Dog:
    # Constructor to initialize attributes
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed  # Attribute

    # Method to display details
    def display_info(self):
        return f"My dog's name is {self.name} and it's a {self.breed}."

# Create an object (instance)
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.display_info())  # Output: My dog's name is Buddy and it's a Golden Retriever.

#Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name  # Public
        self._age = age   # Protected
        self.__salary = 50000  # Private

    def display_salary(self):
        return f"Salary: {self.__salary}"

# Access modifiers
p = Person("Alice", 30)
print(p.name)       # Public: Accessible
print(p._age)       # Protected: Accessible, but should not be modified directly
# print(p.__salary) # Private: Not directly accessible
print(p.display_salary())  # Access private using method

#Inheritance
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return "Some generic sound"

# Child class inheriting from parent class
class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def sound(self):
        return "Bark!"

# Usage
dog = Dog("Canine", "Buddy")
print(dog.species)  # Output: Canine
print(dog.sound())  # Output: Bark!

#Polymorphism
class Bird:
    def fly(self):
        return "Birds can fly."

class Ostrich(Bird):
    def fly(self):
        return "Ostriches can't fly."

# Polymorphism in action
bird = Bird()
ostrich = Ostrich()
print(bird.fly())   # Output: Birds can fly.
print(ostrich.fly()) # Output: Ostriches can't fly.

#Abstract classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# rect = Shape()  # Error: Cannot instantiate abstract class
rect = Rectangle(10, 5)
print(rect.area())  # Output: 50

#Dunder (Magic) Methods
class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Box({self.length}x{self.width})"

    def __add__(self, other):
        return Box(self.length + other.length, self.width + other.width)

box1 = Box(5, 3)
box2 = Box(2, 4)
print(box1)        # Output: Box(5x3)
print(box1 + box2) # Output: Box(7x7)

#Methods
class MyClass:
    class_variable = "I am a class variable"

    def instance_method(self):
        return "Instance method called", self

    @classmethod
    def class_method(cls):
        return "Class method called", cls

    @staticmethod
    def static_method():
        return "Static method called"

obj = MyClass()
print(obj.instance_method())  # Instance method
print(MyClass.class_method()) # Class method
print(MyClass.static_method()) # Static method

#Attributes
class Example:
    class_attr = "Class Attribute"

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

obj1 = Example("Object 1 Attribute")
obj2 = Example("Object 2 Attribute")

print(obj1.class_attr)       # Access class attribute
print(obj1.instance_attr)    # Access instance attribute

#Super
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Call the parent class method
        print("Hello from Child")

c = Child()
c.greet()

#Multiple inheritance
class A:
    def method_a(self):
        return "A"

class B:
    def method_b(self):
        return "B"

class C(A, B):
    pass

obj = C()
print(obj.method_a())  # Output: A
print(obj.method_b())  # Output: B
