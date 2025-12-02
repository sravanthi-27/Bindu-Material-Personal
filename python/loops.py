#1.FOR LOOP

#Iterating through a list:
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)
#Iterating through a string:
for char in "Python":
    print(char)
#Using range():
for i in range(5):  # 0 to 4
    print(i)
#Nested for loops:
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
#terating over a dictionary:
data = {'a': 1, 'b': 2}
for key, value in data.items():
    print(key, value)

#2.WHILE LOOP

#Basic
count = 0
while count<5:
    print(count)
    count += 1
#infinite loop
while True:
    print("Infinite loop")
    break    #stops the loop
#nested while loop
i = 0
while i<3:
    j = 0
    while j<2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

#3.CONTROL STATEMENTS

#using break
for i in range(5):
    if i == 3:
        break
    print(i)
#using continue
for i in range(5):
    if i == 3:
        continue
    print(i)
#using pass
for i in range(5):
    if i==3:
        pass
    print(i)
#using else with loops
for i in range(5):
    print(i)
else:
    print("Loop finished!")
#else with while
count = 0
while count<3:
    print(count)
    count += 1
else:
    print("Condition no longer true")