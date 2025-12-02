def sub(arr, i, target):#Time Complexity: O(2^n),Space Complexity: O(n)

    # Base case
    if target == 0 or i == len(arr):
        return 0

    # If weight is more than capacity, skip it
    if arr[i][0] > target:
        return sub(arr, i + 1, target)

    # Take the item
    take = arr[i][1] + sub(arr, i + 1, target - arr[i][0])

    # Skip the item
    not_take = sub(arr, i + 1, target)

    return max(take, not_take)

# Each item: [weight, value]
arr = [[3, 30], [2, 40], [5, 60]]
capacity = 6
print(sub(arr, 0, capacity))  # Output: 70


#memoization
def sub(arr, i, target, dp):  #Time: O(n * capacity) → because at most n * W unique states are memoized ,space:O(n * capacity) for dp table,O(n)for recursion stack depth
    if i == len(arr) or target == 0:
        return 0

    if dp[i][target] != -1:
        return dp[i][target]

    # Skip current item if its weight is too much
    if arr[i][0] > target:
        dp[i][target] = sub(arr, i + 1, target, dp)
    else:
        take = arr[i][1] + sub(arr, i + 1, target - arr[i][0], dp)
        not_take = sub(arr, i + 1, target, dp)
        dp[i][target] = max(take, not_take)

    return dp[i][target]


# Input
arr = [[3, 30], [2, 40], [5, 60]]
capacity = 6
n = len(arr)

# Create dp table: size n x (capacity + 1)
dp = [[-1 for _ in range(capacity + 1)] for _ in range(n)]

print(sub(arr, 0, capacity, dp))  # Output: 70

#tabulation
def knapsack_tabulation(arr, W):
    n = len(arr)
    
    # Create a 2D dp table with dimensions (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table
    for i in range(1, n + 1):
        wt = arr[i - 1][0]
        val = arr[i - 1][1]
        for w in range(W + 1):
            if wt <= w:
                dp[i][w] = max(dp[i - 1][w], val + dp[i - 1][w - wt])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
arr = [[3, 30], [2, 40], [5, 60]]
W = 6
print(knapsack_tabulation(arr, W))  # Output: 70
#Time and Space Complexity
#Time: O(n * W)
#Space: O(n * W) (can be optimized to O(W) using a 1D array)

