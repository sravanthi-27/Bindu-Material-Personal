def longest_common_subsequence(str1,str2):
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    print(dp)
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[-1][-1]
print(longest_common_subsequence("abcdaf","acbcf"))