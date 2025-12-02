def coin_change(arr,amount):
    dp = [0]*(amount+1)  #bcz we need dp[0] also
    dp[0] = 0
    for i in range(1,amount+1):
        ans = float('inf')
        for j in range(len(arr)):
            if arr[j]<=i:
                rem = i-arr[j]
                ans = min(ans,1+dp[rem])
        dp[i] = ans
    return dp[amount] if amount!=float('inf') else -1
print(coin_change([1,5,6,9],amount=11))
a = [0]*11
print(a,len(a))
