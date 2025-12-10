from collections import Counter

class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        rightCount = Counter(nums)   # counts of values to the right (initially whole array)
        leftCount = Counter()       # counts of values to the left (initially empty)

        ans = 0
        for x in nums:
            # current x is at j: remove it from right (we don't want to count j as k)
            rightCount[x] -= 1

            # number of i with nums[i] == 2*x on the left
            left_needed = leftCount[2 * x]
            # number of k with nums[k] == 2*x on the right
            right_needed = rightCount[2 * x]

            ans = (ans + left_needed * right_needed) % MOD

            # now current x moves to the left for future j's
            leftCount[x] += 1

        return ans
