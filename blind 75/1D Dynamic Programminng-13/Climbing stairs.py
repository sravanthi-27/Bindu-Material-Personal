n = 8 
dp =[1,1]
for i in range(2,n+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n])

#space optimized - o(1)
a, b = 1, 1
for _ in range(2, n + 1):
    a, b = b, a + b
print(b)
