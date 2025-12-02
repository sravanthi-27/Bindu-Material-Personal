#if statement
a = 10
b = 20
if(a<b):
    print("a is less than b")

#if - else statement
if (a == 10):
    print("a value is equal to 10")
else:
    print("a value is not equal to 10")

#if-elif-else statement
if (a == b):
    print("a is equal to b")
elif(a<b):
    print("a is less than b")
else:
    print("a is greater than b")

#Nested if statements
if (a == 10):
    if (a<b):
        print("a is less than b and a value is equal to 10")
    else:
        print("a is greater than b and a value is equal to 10")
else:
    print("a value is not equal to 10")

#Ternary conditional expression
value = a if (a==10) else b
print(value)

#Logical operators
if (a==10) and (a<b):
    print("value of a is 10 and it is less than b")
elif (a==10) or (a>b):
    print("value of a is eual to 10 or a is greater than b")
if not (a==15):
    print("a value is not equal to 15")

#Switch-Case Equivalent (Using Dictionaries)
def switch_case_example(day):
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return switch.get(day, "Invalid day") #the default case is handled using the .get() method's second argument.

print(switch_case_example(3))  # Output: Wednesday
print(switch_case_example(10))  # Output: Invalid day

#Match-Case Statement (Introduced in Python 3.10)
def match_case_example(grade):
    match grade:
        case "A":
            return "Excellent"
        case "B":
            return "Good"
        case "C":
            return "Average"
        case "D":
            return "Poor"
        case _:
            return "Invalid grade"

print(match_case_example("A"))  # Output: Excellent
print(match_case_example("E"))  # Output: Invalid grade

#Assertions
def divide_numbers(a, b):
    assert b != 0, "Divider cannot be zero"
    return a / b

print(divide_numbers(10, 2))  # Output: 5.0
#print(divide_numbers(10, 0))  # Raises AssertionError: Divider cannot be zero

#Exception Handling with Conditions
def exception_handling_example(number):
    try:
        result = 10 / number
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Input must be a number.")
    else:
        print("Division successful!")
    finally:
        print("Execution completed.")

exception_handling_example(2)  # Output: Result: 5.0, Division successful!, Execution completed.
exception_handling_example(0)  # Output: Cannot divide by zero., Execution completed.
exception_handling_example("a")  # Output: Input must be a number., Execution completed.
