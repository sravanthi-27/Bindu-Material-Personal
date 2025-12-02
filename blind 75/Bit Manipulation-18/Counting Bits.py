n = 5 
arr = []
for i in range(n+1):
    count = 0
    x = i
    while x:
        x &= x-1
        count += 1
    arr.append(count)
print(arr)