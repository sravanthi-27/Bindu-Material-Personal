arr = [7,1,5,3,6,4]
maxi = float('-inf')
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        diff = arr[j]-arr[i]
        maxi = max(maxi,diff)
print(maxi)

#optimal
mini = float('inf')
profit = 0
for i in range(len(arr)):
    mini = min(mini,arr[i])
    difference = arr[i]-mini 
    profit=max(profit,difference)
print(profit)