#recursion approach -time,space:o(n.2^n)-2^n subsequences,n- path
def subsequence(nums, i, res, path):
    # Base case: end of list
    if i == len(nums):
        if len(path) >= 1:         # Only keep subsequences of length > 1
            res.append(path)
        return

    # Include current element if path is empty or increasing
    if not path or nums[i] > path[-1]:
        subsequence(nums, i + 1, res, path + [nums[i]])

    # Exclude current element
    subsequence(nums, i + 1, res, path)

# Input
nums = [10, 9, 2, 5, 3, 7, 101, 18]
res = []

# Function call
subsequence(nums, 0, res, [])
maxlen = 0
# Print result
print("All increasing subsequences:")
for seq in res:
    print(seq)
    length = len(seq)
    maxlen = max(maxlen,length)
print(maxlen)


#recursion approach 2 by using prev index
def sub(arr,index,prev_index): #time:O(2^n),space:O(n)-stack space
    if index==len(arr):
       return 0
    length = 0 + sub(arr,index+1,prev_index) #exclude current elem,0 bcz we are not increasing length
    if prev_index==-1 or arr[index]>arr[prev_index]:
      length = max(length,1+sub(arr,index+1,index))
    return length
    
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(sub(arr,0,-1)) #initially previndex is -1 bcz we didnt select anything

#memoization-still not optimal
def sub(arr, index, prev_index, dp): #time:0(n*n),space:O(n*n)+O(n)
    if index == len(arr):
        return 0

    if dp[index][prev_index + 1] != -1:
        return dp[index][prev_index + 1]

    # Exclude current element
    length = sub(arr, index + 1, prev_index, dp)

    # Include current element if increasing
    if prev_index == -1 or arr[index] > arr[prev_index]:
        length = max(length, 1 + sub(arr, index + 1, index, dp))

    dp[index][prev_index + 1] = length
    return dp[index][prev_index + 1] 
# Input
arr = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(arr)

# Memoization table: n x (n+1), prev_index can be -1 to n-1 → offset by +1
dp = [[-1 for _ in range(n + 1)] for _ in range(n)] #n+1 bcz we are trying store index -1 at 0 and index1 at index0 and so on now it becomes len(dp[rows])=len(arr),len(dp[cols])=len(arr)+1

print(sub(arr, 0, -1, dp))  # Output: Length of LIS

#tabulation  -time:O(n^2),space:O(n)
def tabulation_lis(arr):
    n = len(arr)
    dp = [1] * n  # dp[i] = length of LIS ending at index i

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:  # valid increasing pair
                dp[i] = max(dp[i], dp[j] + 1)

    return dp  # max of all LIS lengths

# Input
arr = [5,4,11,1,16,8]
print(tabulation_lis(arr))  # Output: 4


#binary search
def binary_search_replace(res, target):
    left, right = 0, len(res) - 1
    while left <= right:
        mid = (left + right) // 2
        if res[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    res[left] = target  # replace with smaller value

arr = [1,4,5,4,2,8]
res = [arr[0]]  # Start with the first element

for i in range(1, len(arr)):
    if arr[i] > res[-1]:
        res.append(arr[i])
    else:
        binary_search_replace(res, arr[i])

print("LIS length:", len(res))
print("Subsequence approximation:", res)
