class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = a & b        # find carry
            a = a ^ b            # add without carry
            b = carry << 1       # move carry left
        return a
