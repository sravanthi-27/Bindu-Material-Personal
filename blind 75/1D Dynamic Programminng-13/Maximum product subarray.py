class Solution:
    def maxProduct(self, nums) -> int:
        prefix,suffix,maxi = 1,1,float('-inf')
        n=len(nums)
        for i in range(len(nums)):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix *= nums[i]
            suffix*=nums[n-i-1]
            maxi = max(maxi,max(prefix,suffix))
        return maxi 