#Basic exception handling:try and except
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a number.")

#Handling multiple extensions
   #Using multiple excepts
try:
    result = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
    #Using single except
try:
    result = 10 / int(input("Enter a number: "))
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

#Else clause
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"The number is: {num}")

#Finally clause
try:
    file = open("example.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
    print("File closed.")

#Raising exceptions
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")
else:
    print(f"Your age is {age}.")

#Creating custom exceptions
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError
except NegativeNumberError as e:
    print(e)


#FILE HANDLING WITH EXCEPTION HANDLING

#Reading a file
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

#Writing to a file
try:
    with open("output.txt", "w") as file:
        file.write("This is a test message.")
        print("Data written to the file.")
except IOError:
    print("An error occurred while writing to the file.")

#Appending to a file
try:
    with open("output.txt", "a") as file:
        file.write("\nAppending more data.")
        print("Data appended to the file.")
except IOError:
    print("An error occurred while appending to the file.")

#Handling exceptions with file operations
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist!")
except IOError:
    print("An I/O error occurred.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")

#Reading line by line
try:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found!")

#Nested try-except
try:
    with open("example.txt", "r") as file:
        try:
            data = file.read()
            print(int(data))  # Trying to convert file content to an integer
        except ValueError:
            print("The file does not contain a valid number.")
except FileNotFoundError:
    print("File not found!")
