n = 12
a = bin(n)
count = 0 
a = str(a)
for i in range(len(a)):
    if a[i]=="1":
        count+=1
print(count)