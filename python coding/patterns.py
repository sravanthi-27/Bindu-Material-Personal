'''print("1st pattern - Right angled triangle:")
for i in range(5):     #Rows
    for j in range(i):    #Columns
      print("*" ,  end = ' ' )      #when j = 0 it prints an empty line
    print()

print("Numbers pattern")
for i in range(1,6):
    for j in range(1,i):
        print(j, end=" ")
    print()

print("2nd Pattern - Inverted Right-Angled traingle")
for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()

print("Inverted numbers pattern")
for i in range(1,7):
    for j in range(1,6-i):
        print(j,end=" ")
    print()


print("3rd pattern - Pyramid")
rows = 5  # Number of rows for the pyramid
for i in range(1, rows + 1):  # Loop for each row
    for j in range(rows - i):  # Loop for printing spaces
        print(" ", end="")
    for k in range(i):  # Loop for printing stars
        print("* ", end="")
    print()  # Move to the next line

print("4th pattern - Inverted Pyramid Pattern")
rows = 5
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end = "")
    for k in range(i):
        print("*" , end = " ")
    print()'''

rows = 4
for i in range(1,rows + 1):
    print(" "*(rows-i) + "#"*i)