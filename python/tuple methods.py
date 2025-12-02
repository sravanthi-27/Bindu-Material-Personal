#Built-in functions
 
#Count
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))  # Output: 3

#Index
t = (1, 2, 3, 2, 4)
print(t.index(2))  # Output: 1
print(t.index(2, 2))  # Output: 3 (starts searching from index 2)

#length
t = (1, 2, 3)
print(len(t))  # Output: 3

#max
t = (1, 2, 3)
print(max(t))  # Output: 3

#min
t = (1, 2, 3)
print(min(t))  # Output: 1

#sum
t = (1, 2, 3)
print(sum(t))  # Output: 6

#sorted
t = (3, 1, 2)
print(sorted(t))  # Output: [1, 2, 3]

#any
t = (0, 0, 1)
print(any(t))  # Output: True

#all
t = (1, 2, 3)
print(all(t))  # Output: True

#Own functions

#count method
def tuple_count(t, value):
    count = 0
    for element in t:
        if element == value:
            count += 1
    return count
t = (1, 2, 3, 2, 4, 2)
print(tuple_count(t, 2))  # Output: 3

#Index method
def tuple_index(t, value, start=0, end=None):
    if end is None:
        end = len(t)
    for i in range(start, end):
        if t[i] == value:
            return i
    raise ValueError(f"{value} is not in tuple")
t = (1, 2, 3, 4, 5)
print(tuple_index(t, 3))  # Output: 2
print(tuple_index(t, 4, 2))  # Output: 3

#Slicing
def tuple_slice(t, start=0, end=None, step=1):
    if end is None:
        end = len(t)
    result = ()
    for i in range(start, end, step):
        result += (t[i],)
    return result
t = (1, 2, 3, 4, 5)
print(tuple_slice(t, 1, 4))  # Output: (2, 3, 4)

#Reversing
def tuple_reverse(t):
    result = ()
    for i in range(len(t) - 1, -1, -1):
        result += (t[i],)
    return result
t = (1, 2, 3, 4)
print(tuple_reverse(t))  # Output: (4, 3, 2, 1)

#Sorting
def tuple_sort(t):
    t_list = list(t)
    for i in range(len(t_list)):
        for j in range(len(t_list) - i - 1):
            if t_list[j] > t_list[j + 1]:
                t_list[j], t_list[j + 1] = t_list[j + 1], t_list[j]
    return tuple(t_list)
t = (3, 1, 4, 2)
print(tuple_sort(t))  # Output: (1, 2, 3, 4)

#Concatenation
def tuple_concat(t1, t2):
    result = t1 + t2
    return result
t1 = (1, 2)
t2 = (3, 4)
print(tuple_concat(t1, t2))  # Output: (1, 2, 3, 4)

#Length
def tuple_length(t):
    length = 0
    for _ in t:
        length += 1
    return length
t = (1, 2, 3)
print(tuple_length(t))  # Output: 3

#Maximum value
def tuple_max(t):
    max_val = t[0]
    for element in t:
        if element > max_val:
            max_val = element
    return max_val
t = (1, 2, 3, 4, 5)
print(tuple_max(t))  # Output: 5

#Minimum value
def tuple_min(t):
    min_val = t[0]
    for element in t:
        if element < min_val:
            min_val = element
    return min_val
t = (1, 2, 3, 4, 5)
print(tuple_min(t))  # Output: 1

#Sum
def tuple_sum(t):
    total = 0
    for element in t:
        total += element
    return total
t = (1, 2, 3)
print(tuple_sum(t))  # Output: 6

#Check if Element Exists (like in)
def tuple_contains(t, value):
    for element in t:
        if element == value:
            return True
    return False
t = (1, 2, 3)
print(tuple_contains(t, 2))  # Output: True
print(tuple_contains(t, 5))  # Output: False

#Unpacking
def tuple_unpack(t):
    return [*t]
t = (10, 20, 30)
a, b, c = tuple_unpack(t)
print(a, b, c)  # Output: 10 20 30
