d = {}
key = [1, 0, 0]
d[key] = "value"  # ❌ TypeError: unhashable type: 'list' in dictionaries we cant use list as keys so convert into tuple and then use 
print(d)

#Clear
my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # Output: {}

#Copy
my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2'}

#fromkeys
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

#get
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))  # Output: 1
print(my_dict.get('c', 'Not Found'))  # Output: Not Found

#items
my_dict = {'a': 1, 'b': 2}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])

#keys
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

#values
my_dict = {'a': 1, 'b': 2}
print(my_dict.values())  # Output: dict_values([1, 2])

#deleting elements using index is not possible

#pop
my_dict = {'a': 1, 'b': 2}
print(my_dict.pop('a'))  # Output: 1
print(my_dict)  # Output: {'b': 2}

#Popitem
my_dict = {'a': 1, 'b': 2}
print(my_dict.popitem())  # Output: ('b', 2)
print(my_dict)  # Output: {'a': 1}

#setdefault
my_dict = {'a': 1}
print(my_dict.setdefault('b', 2))  # Output: 2
print(my_dict)  # Output: {'a': 1, 'b': 2}

#Update
my_dict = {'a': 1}
my_dict.update({'b': 2, 'c': 3})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

#delete
my_dict = {'a': 1, 'b': 2}
del my_dict['a']
print(my_dict)  # Output: {'b': 2}

#sort by frequency
di = {'t': 1, 'r': 1, 'e': 2}
sorted_dict = dict(sorted(di.items(), key=lambda item: item[1],reverse = True))

#Own functions
class MyDictionary:
    def __init__(self):
        self.data = []

    def add(self, key, value):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data[i][1] = value  # Update the value if the key exists
                return
        self.data.append([key, value])  # Add a new key-value pair

    def get(self, key, default=None):
        for k, v in self.data:
            if k == key:
                return v
        return default  # Return default if key not found

    def remove(self, key):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data.pop(i)
                return True
        return False  # Key not found

    def contains(self, key):
        for k, _ in self.data:
            if k == key:
                return True
        return False

    def keys(self):
        return [k for k, _ in self.data]

    def values(self):
        return [v for _, v in self.data]

    def items(self):
        return self.data[:]

    def clear(self):
        self.data = []

    def size(self):
        return len(self.data)

    def display(self):
        print("{", end="")
        print(", ".join(f"{repr(k)}: {repr(v)}" for k, v in self.data), end="")
        print("}")

# Example Usage
my_dict = MyDictionary()
my_dict.add("a", 1)
my_dict.add("b", 2)
my_dict.add("a", 3)  # Updates key 'a'
print(my_dict.get("a"))  # Output: 3
print(my_dict.contains("c"))  # Output: False
my_dict.display()  # Output: {'a': 3, 'b': 2}
my_dict.remove("b")
my_dict.display()  # Output: {'a': 3}

#mimic functions

#get
def custom_get(data, key, default=None):
    for k, v in data:
        if k == key:
            return v
    return default

# Example Usage
data = [["a", 1], ["b", 2]]
print(custom_get(data, "a"))  # Output: 1
print(custom_get(data, "c", "Not Found"))  # Output: Not Found

#update
def custom_update(data, updates):
    for key, value in updates:
        found = False
        for item in data:
            if item[0] == key:
                item[1] = value
                found = True
                break
        if not found:
            data.append([key, value])

# Example Usage
data = [["a", 1], ["b", 2]]
updates = [["b", 3], ["c", 4]]
custom_update(data, updates)
print(data)  # Output: [['a', 1], ['b', 3], ['c', 4]]

#pop
def custom_pop(data, key):
    for i in range(len(data)):
        if data[i][0] == key:
            value = data[i][1]
            del data[i]
            return value
    raise KeyError(f"Key {key} not found!")

# Example Usage
data = [["a", 1], ["b", 2]]
print(custom_pop(data, "a"))  # Output: 1
print(data)  # Output: [['b', 2]]

#fromkeys
def custom_fromkeys(keys, value=None):
    result = []
    for key in keys:
        result.append([key, value])
    return result

# Example Usage
keys = ["a", "b", "c"]
result = custom_fromkeys(keys, 0)
print(result)  # Output: [['a', 0], ['b', 0], ['c', 0]]

#Clear
def custom_clear(data):
    while data:
        data.pop()

# Example Usage
data = [["a", 1], ["b", 2]]
custom_clear(data)
print(data)  # Output: []

#Items
def custom_items(data):
    return [(k, v) for k, v in data]

# Example Usage
data = [["a", 1], ["b", 2]]
print(custom_items(data))  # Output: [('a', 1), ('b', 2)]

#Keys
def custom_keys(data):
    return [k for k, _ in data]

# Example Usage
data = [["a", 1], ["b", 2]]
print(custom_keys(data))  # Output: ['a', 'b']

#Values
def custom_values(data):
    return [v for _, v in data]

# Example Usage
data = [["a", 1], ["b", 2]]
print(custom_values(data))  # Output: [1, 2]

#setdefault
def custom_setdefault(data, key, default=None):
    for k, v in data:
        if k == key:
            return v
    data.append([key, default])
    return default

# Example Usage
data = [["a", 1]]
print(custom_setdefault(data, "b", 2))  # Output: 2
print(data)  # Output: [['a', 1], ['b', 2]]
