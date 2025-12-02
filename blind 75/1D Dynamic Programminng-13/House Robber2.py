nums = [1,2,3]
n = len(nums)
def loot(nums):
    if not nums:
        return 0
    elif len(nums)<2:
        return (nums[0])
    else:
        dp =[0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
def res(nums):
    a = loot(nums[:len(nums)-1])
    b = loot(nums[1:])
    return max(a,b)
print(res(nums))