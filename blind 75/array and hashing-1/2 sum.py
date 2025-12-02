#brute force
arr=[2,6,5,8,11]
target=14
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print([i,j])

#return indexes
hashmap = {}
arr=[2,6,5,8,11]
target=14
for i in range(len(arr)):
    diff = target-arr[i]
    if diff in hashmap:
        print(hashmap[diff],i)
    hashmap[arr[i]]=i

# if we need to return print or false
arr = [2,6,5,8,11]
arr.sort()
left,right = 0,len(arr)-1
flag=False
target=14
while left<right:
    if arr[left]+arr[right]==target:
        flag=True
        break 
    if arr[left]+arr[right]>target:
        right-=1
    else:
        left+=1
print(flag)