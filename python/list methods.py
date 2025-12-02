#Built-in methods
# #append
l1 = [1,2,3]
l1.append(4)
print("append:",l1)

#extend
l2 = [1,2,3]
l2.extend([4,5])
print("extendl:",2)

#insert
l3 = [1,2,3]
l3.insert(1, "a")      #insert a at index 1
print("insert:",l3)

#remove
l4 = [1,2,3,2]
l4.remove(2)  #removes the first occurence of 2
print("remove:",l4)

#pop
l5 = [1,2,3]
l5.pop()
print("pop:",l5)   #removes the last element

#clear
l6 = [1,2,3]
l6.clear()
print("clear:",l6)

#index
l7 = [1,2,3]
print("index:",l7.index(2))       #returns the index of first occurence of a specified element

#count
l8 = [1,2,3,2]
print("count:",l8.count(2))     #returns the number of occurences of a specified element

#sort
l9 = [1,4,2,3]
l9.sort()
print("sort methods:",l9)

l9 = [1, 4, 2, 3]
print(l9.sort())#The sort() method is called on l9, which sorts the list in place.However, sort() does not return anything. It modifies the list and returns None.you are printing the return value of l9.sort(), which is None.

#sorted
l9 = [1, 4, 2, 3]
sorted_l9 = sorted(l9)
print(sorted_l9)  # Output: [1, 2, 3, 4]
print(l9)         # Original list remains unchanged: [1, 4, 2, 3]

#sorting based on key
arr = [["a1",0,6],["a2",3,4],["a3",1,2],["a4",5,9],["a5",5,7],["a6",8,9]]
arr.sort(key=lambda x:(x[2]))

#reverse
l10 = [1,2,3]
l10.reverse()
print("reverse:",l10)

#copy
l11 = [1,2,3]
new_lst = l11.copy()
print("copy:",new_lst)

#Examples of combined usage
#1.Add multiple elements and sort
lst = [5,1,3]
lst.extend([6,7])
lst.sort()
print("Adding and sorting elements:",lst)

#2.Remove duplicates using count and remove methods
lst = [1,2,3,2,5]
for elem in lst:
    if lst.count(elem)>1:
        lst.remove(elem)
print("removing duplicates:",lst)

print("Inserting methods")
#Inserting elements at particular place
#Insert an element into the middle of a list:
lst = [1, 2, 4, 5]
lst.insert(2, 3)  # Insert 3 at index 2
print(lst)  # Output: [1, 2, 3, 4, 5]

#Insert at beginning
lst = [2, 3, 4]
lst.insert(0, 1)  # Insert 1 at index 0
print(lst)  # Output: [1, 2, 3, 4]

#Insert at end
lst = [1, 2, 3]
lst.insert(len(lst), 4)  # Insert 4 at the end
print(lst)  # Output: [1, 2, 3, 4]

#Insert in an empty list
lst = []
lst.insert(0, 10)  # Insert 10 at index 0
print(lst)  # Output: [10]

#Insert an element in a negative index
lst = [1, 2, 3, 4]
lst.insert(-1, 99)  # Insert 99 before the last element
print(lst)  # Output: [1, 2, 3, 99, 4]


#Example with Out-of-Range Index:

lst = [1, 2, 3]
lst.insert(10, 4)  # Inserts 4 at the end
print(lst)  # Output: [1, 2, 3, 4]

lst.insert(-10, 0)  # Inserts 0 at the beginning
print(lst)  # Output: [0, 1, 2, 3, 4]

#own functions

#Append
def my_append(lst, element):
    lst += [element]
    return lst
lst = [1, 2, 3]
print(my_append(lst, 4))  # Output: [1, 2, 3, 4]

#Insert
def my_insert(lst, index, element):
    return lst[:index] + [element] + lst[index:]
lst = [1, 2, 4]
print(my_insert(lst, 2, 3))  # Output: [1, 2, 3, 4]

#Remove
def my_remove(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return lst[:i] + lst[i+1:]
    return lst
lst = [1, 2, 3, 2]
print(my_remove(lst, 2))  # Output: [1, 3, 2]

#pop
def my_pop(lst, index=-1):
    if index < 0:
        index += len(lst)
    element = lst[index]
    lst = lst[:index] + lst[index+1:]
    return element, lst
lst = [1, 2, 3, 4]
element, lst = my_pop(lst)
print(element)  # Output: 4
print(lst)      # Output: [1, 2, 3]

#count
def my_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
lst = [1, 2, 3, 2]
print(my_count(lst, 2))  # Output: 2

#Index
def my_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    raise ValueError(f"{element} is not in the list")
lst = [1, 2, 3]
print(my_index(lst, 2))  # Output: 1

#Reverse
def my_reverse(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
lst = [1, 2, 3]
print(my_reverse(lst))  # Output: [3, 2, 1]

#Sort
def my_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
lst = [4, 2, 3, 1]
print(my_sort(lst))  # Output: [1, 2, 3, 4]

#Extend
def my_extend(lst, elements):
    for element in elements:
        lst += [element]
    return lst
lst = [1, 2]
print(my_extend(lst, [3, 4]))  # Output: [1, 2, 3, 4]

#Copy
def my_copy(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item)
    return new_lst
lst = [1, 2, 3]
copy_lst = my_copy(lst)
print(copy_lst)  # Output: [1, 2, 3]

#clear
def my_clear(lst):
    return []
lst = [1, 2, 3]
lst = my_clear(lst)
print(lst)  # Output: []

#Max
def my_max(lst):
    max_element = lst[0]
    for item in lst:
        if item > max_element:
            max_element = item
    return max_element
lst = [1, 5, 3, 2]
print(my_max(lst))  # Output: 5

#Min
def my_min(lst):
    min_element = lst[0]
    for item in lst:
        if item < min_element:
            min_element = item
    return min_element
lst = [1, 5, 3, 2]
print(my_min(lst))  # Output: 1

#Sum
def my_sum(lst):
    total = 0
    for item in lst:
        total += item
    return total
lst = [1, 2, 3]
print(my_sum(lst))  # Output: 6

#Sliced list
def my_slice(lst, start, end=None):
    if end is None:
        end = len(lst)
    sliced_lst = []
    for i in range(start, end):
        sliced_lst += [lst[i]]
    return sliced_lst
lst = [1, 2, 3, 4]
print(my_slice(lst, 1, 3))  # Output: [2, 3]

#List with all types
all_types_list = [
    42,                             # Integer
    3.14,                           # Float
    True,                           # Boolean
    "Hello, World!",                # String
    [1, 2, 3],                      # List
    (4, 5, 6),                      # Tuple
    {7, 8, 9},                      # Set
    {'key': 'value', 'pi': 3.14},   # Dictionary
    None,                           # NoneType
    b"bytes",                       # Bytes
    bytearray(b"byte array"),       # Bytearray
    memoryview(b"memory view"),     # Memoryview
    complex(2, 3),                  # Complex Number
    range(5),                       # Range
    frozenset([10, 11, 12]),        # Frozenset
    lambda x: x * 2,                # Function (Lambda)
    Exception("An error occurred")  # Exception (Object)
]

# Example: Accessing all types
for i, item in enumerate(all_types_list):
    print(f"Item {i}: {item} (Type: {type(item)})")
