# Example string
s = "hello world"
s2 = "Python123"
s3 = "    space    "
s4 = "12345"

# String Methods with Examples

# 1. capitalize()
print(s.capitalize())  # "Hello world"

# 2. casefold()
print(s2.casefold())  # "python123"

# 3. center()
print(s.center(20, '-'))  # "-----hello world-----"

# 4. count()
print(s.count('o'))  # 2

# 5. encode()
print(s.encode())  # b'hello world'

# 6. endswith()
print(s.endswith('world'))  # True

# 7. expandtabs()
tabbed_string = "hello\tworld"
print(tabbed_string.expandtabs(4))  # "hello   world"

# 8. find()
print(s.find('o'))  # 4

# 9. format()
print("Hello, {}!".format("Alice"))  # "Hello, Alice!"

# 10. format_map()
print("{name}".format_map({"name": "Bob"}))  # "Bob"

# 11. index()
print(s.index('o'))  # 4

# 12. isalnum()
print(s2.isalnum())  # True

# 13. isalpha()
print("Python".isalpha())  # True

# 14. isascii()
print(s.isascii())  # True

# 15. isdecimal()
print(s4.isdecimal())  # True

# 16. isdigit()
print(s4.isdigit())  # True

# 17. isidentifier()
print("my_var".isidentifier())  # True

# 18. islower()
print(s.islower())  # True

# 19. isnumeric()
print(s4.isnumeric())  # True

# 20. isprintable()
print(s.isprintable())  # True

# 21. isspace()
print("   ".isspace())  # True

# 22. istitle()
print("Hello World".istitle())  # True

# 23. isupper()
print("HELLO".isupper())  # True

# 24. join()
print(", ".join(["a", "b", "c"]))  # "a, b, c"

# 25. ljust()
print(s.ljust(15, '-'))  # "hello world----"

# 26. lower()
print("HELLO".lower())  # "hello"

# 27. lstrip()
print(s3.lstrip())  # "space    "

# 28. maketrans() + translate()
trans = str.maketrans("aeiou", "12345")
print("hello".translate(trans))  # "h2ll4"

# 29. partition()
print(s.partition(" "))  # ('hello', ' ', 'world')

# 30. replace()
print(s.replace("world", "Python"))  # "hello Python"

# 31. rfind()
print(s.rfind("o"))  # 7

# 32. rindex()
print(s.rindex("o"))  # 7

# 33. rjust()
print(s.rjust(15, '-'))  # "----hello world"

# 34. rpartition()
print(s.rpartition(" "))  # ('hello', ' ', 'world')

# 35. rsplit()
print(s.rsplit(" ", 1))  # ['hello', 'world']

# 36. rstrip()
print(s3.rstrip())  # "    space"

# 37. split()
print(s.split(" "))  # ['hello', 'world']

# 38. splitlines()
print("hello\nworld".splitlines())  # ['hello', 'world']

# 39. startswith()
print(s.startswith("hello"))  # True

# 40. strip()
print(s3.strip())  # "space"

# 41. swapcase()
print("Hello World".swapcase())  # "hELLO wORLD"

# 42. title()
print(s.title())  # "Hello World"

# 43. upper()
print(s.upper())  # "HELLO WORLD"

# 44. zfill()
print(s.zfill(15))  # "00000hello world"

#Own functions

# Custom Implementation of String Methods

# 1. capitalize()
def custom_capitalize(string):
    if not string:
        return string
    return string[0].upper() + string[1:].lower()

print(custom_capitalize("hello WORLD"))  # "Hello world"

# 2. casefold()
def custom_casefold(string):
    return "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in string)

print(custom_casefold("HELLO World"))  # "hello world"

# 3. center()
def custom_center(string, width, fillchar=' '):
    if len(string) >= width:
        return string
    total_pad = width - len(string)
    left_pad = total_pad // 2
    right_pad = total_pad - left_pad
    return fillchar * left_pad + string + fillchar * right_pad

print(custom_center("hello", 10, '-'))  # "--hello---"

# 4. count()
def custom_count(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

print(custom_count("banana", "a"))  # 3

# 5. endswith()
def custom_endswith(string, suffix):
    return string[-len(suffix):] == suffix if len(suffix) <= len(string) else False

print(custom_endswith("hello", "lo"))  # True

# 6. find()
def custom_find(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i
    return -1

print(custom_find("hello world", "world"))  # 6

# 7. isalpha()
def custom_isalpha(string):
    return all(('a' <= c <= 'z' or 'A' <= c <= 'Z') for c in string)

print(custom_isalpha("hello"))  # True
print(custom_isalpha("hello123"))  # False

# 8. isdigit()
def custom_isdigit(string):
    return all('0' <= c <= '9' for c in string)

print(custom_isdigit("12345"))  # True
print(custom_isdigit("123a"))  # False

# 9. join()
def custom_join(separator, iterable):
    result = ""
    for index, item in enumerate(iterable):
        if index > 0:
            result += separator
        result += item
    return result

print(custom_join(", ", ["a", "b", "c"]))  # "a, b, c"

# 10. lower()
def custom_lower(string):
    return "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in string)

print(custom_lower("HELLO"))  # "hello"

# 11. replace()
def custom_replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i + len(old)] == old:
            result += new
            i += len(old)
        else:
            result += string[i]
            i += 1
    return result

print(custom_replace("banana", "a", "o"))  # "bonono"

# 12. split()
def custom_split(string, separator):
    result = []
    current = ""
    for char in string:
        if char == separator:
            result.append(current)
            current = ""
        else:
            current += char
    result.append(current)
    return result

print(custom_split("a,b,c", ","))  # ['a', 'b', 'c']

# 13. startswith()
def custom_startswith(string, prefix):
    return string[:len(prefix)] == prefix

print(custom_startswith("hello", "he"))  # True

# 14. strip()
def custom_strip(string):
    start, end = 0, len(string) - 1
    while start <= end and string[start] == ' ':
        start += 1
    while end >= start and string[end] == ' ':
        end -= 1
    return string[start:end + 1]

print(custom_strip("   hello   "))  # "hello"

# 15. upper()
def custom_upper(string):
    return "".join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in string)

print(custom_upper("hello"))  # "HELLO"

# 16. zfill()
def custom_zfill(string, width):
    if len(string) >= width:
        return string
    return '0' * (width - len(string)) + string

print(custom_zfill("42", 5))  # "00042"

