n = int(input("For end:"))
for i in range(n):
    for j in range(n-1):
        print(i , end = " ")
        
n = int(input("For end method2:"))
for i in range(n):
    for j in range(n-1):
        print(i , end = "*")

n = int(input("for end 3rd method:"))
for i in range(n):
    for j in range(n-1):
        print(i , end = "\n")


#default behaviour separated by spaces
print("end over \n SEp methods:")
print("Python" , "is" , "awesome")
print("2024" , "02" , "03" , sep = "-")
print("Bindu" , "CSE" , "Student" , sep=' ')
print("A" , "B" , "C" , sep = '***')
print("Miriyala" , "Bindu" , "Sravanthi" , sep = "\n")