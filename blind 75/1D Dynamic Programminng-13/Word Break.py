def wordBreak(s, wordDict):
    maxlen = max(len(word) for word in wordDict)  # Find max word length
    wordSet = set(wordDict)  # Convert list to set for O(1) lookup
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case: empty string can always be segmented

    for i in range(1, len(s) + 1):
        for j in range(max(0, i - maxlen), i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[-1]
