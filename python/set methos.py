#Built-in functions

#Add
s = {1,2,3}
s.add(4)
print(s)

#Clear
s={1,2,3}
s.clear()
print(s)

#Copy
s = {1,2,3}
s_copy = s.copy()
print(s_copy)

#Difference
s1 = {1,2,3}
s2 = {3,4,5}
print(s1.difference(s2))

#Difference_update(sets)
s1 = {1,2,3}
s2 = {3,4,5}
s1.difference_update(s2)
print(s1)

#Discard element
s = {1,2,3}
result = s.discard(2)
print(result)
print(s)

#Intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.intersection(s2))  # {2, 3}

#Intersection_update
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.intersection_update(s2)  # s1 = {2, 3}
print(s1)

#isdisjoint(other_set)
s1 = {1, 2}
s2 = {3, 4}
print(s1.isdisjoint(s2))  # True

#issubset(other_set)
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))  # True

#issuperset(other_set)
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))  # True

#Pop
s = {1, 2, 3}
elem = s.pop()  # Removes any element
print(elem)
print(s)

#Remove element
s = {1, 2, 3}
s.remove(2)  # s = {1, 3}
print(s)

#Symmetric_difference(other-set)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.symmetric_difference(s2))  # {1, 2, 4, 5}

#symmetric_difference_update(other_set)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.symmetric_difference_update(s2)  # s1 = {1, 2, 4, 5}

#Union
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))  # {1, 2, 3, 4, 5}

#update
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.update(s2)  # s1 = {1, 2, 3, 4, 5}

#Own functions

# Custom add function
def add_to_set(s, element):
    if element not in s:
        s.append(element)

# Custom clear function
def clear_set(s):
    s.clear()

# Custom copy function
def copy_set(s):
    return s[:]

# Custom difference function
def difference_set(s1, s2):
    return [item for item in s1 if item not in s2]

# Custom difference_update function
def difference_update_set(s1, s2):
    for item in s2:
        if item in s1:
            s1.remove(item)

# Custom discard function
def discard_from_set(s, element):
    if element in s:
        s.remove(element)

# Custom intersection function
def intersection_set(s1, s2):
    return [item for item in s1 if item in s2]

# Custom intersection_update function
def intersection_update_set(s1, s2):
    s1[:] = [item for item in s1 if item in s2]

# Custom isdisjoint function
def isdisjoint_set(s1, s2):
    for item in s1:
        if item in s2:
            return False
    return True

# Custom issubset function
def issubset_set(s1, s2):
    for item in s1:
        if item not in s2:
            return False
    return True

# Custom issuperset function
def issuperset_set(s1, s2):
    for item in s2:
        if item not in s1:
            return False
    return True

# Custom pop function
def pop_from_set(s):
    if s:
        return s.pop(0)  # Remove the first element
    else:
        raise KeyError("pop from an empty set")

# Custom remove function
def remove_from_set(s, element):
    if element in s:
        s.remove(element)
    else:
        raise KeyError(f"{element} not found in set")

# Custom symmetric_difference function
def symmetric_difference_set(s1, s2):
    return [item for item in s1 if item not in s2] + [item for item in s2 if item not in s1]

# Custom symmetric_difference_update function
def symmetric_difference_update_set(s1, s2):
    s1[:] = symmetric_difference_set(s1, s2)

# Custom union function
def union_set(s1, s2):
    result = s1[:]
    for item in s2:
        if item not in result:
            result.append(item)
    return result

# Custom update function
def update_set(s1, s2):
    for item in s2:
        if item not in s1:
            s1.append(item)

# Example Usage
set1 = [1, 2, 3]
set2 = [3, 4, 5]

# Add
add_to_set(set1, 6)
print("After add:", set1)  # [1, 2, 3, 6]

# Clear
clear_set(set1)
print("After clear:", set1)  # []

# Copy
set1 = [1, 2, 3]
set_copy = copy_set(set1)
print("Copy:", set_copy)  # [1, 2, 3]

# Difference
print("Difference:", difference_set(set1, set2))  # [1, 2]

# Difference Update
difference_update_set(set1, set2)
print("After difference update:", set1)  # [1, 2]

# Discard
discard_from_set(set1, 2)
print("After discard:", set1)  # [1]

# Intersection
print("Intersection:", intersection_set(set1, set2))  # []

# Intersection Update
intersection_update_set(set1, set2)
print("After intersection update:", set1)  # []

# Is Disjoint
print("Is Disjoint:", isdisjoint_set(set1, set2))  # True

# Is Subset
print("Is Subset:", issubset_set(set1, set2))  # True

# Is Superset
print("Is Superset:", issuperset_set(set1, set2))  # False

# Pop
set1 = [1, 2, 3]
print("Pop:", pop_from_set(set1))  # 1

# Remove
remove_from_set(set1, 2)
print("After remove:", set1)  # [3]

# Symmetric Difference
set1 = [1, 2, 3]
print("Symmetric Difference:", symmetric_difference_set(set1, set2))  # [1, 2, 4, 5]

# Symmetric Difference Update
symmetric_difference_update_set(set1, set2)
print("After symmetric difference update:", set1)  # [1, 2, 4, 5]

# Union
print("Union:", union_set([1, 2], [2, 3]))  # [1, 2, 3]

# Update
set1 = [1, 2]
update_set(set1, [3, 4])
print("After update:", set1)  # [1, 2, 3, 4]
