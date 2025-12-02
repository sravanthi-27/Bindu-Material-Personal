nums = [0, 1]
for i in range(len(nums)+1):
    if i not in nums:
        print(i)

# bit manipulation approach 
class Solution:
    def missingNumber(self, nums) -> int:
        xor = 0
        n = len(nums)

        for i in range(n+1):
            xor ^= i     # XOR all numbers 0..n
        
        for num in nums:
            xor ^= num   # XOR all numbers in the array

        return xor       # remaining value is the missing number
