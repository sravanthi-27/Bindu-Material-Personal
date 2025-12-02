# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        def maxpath(node):
            if not node:
                return 0

            leftsum = max(maxpath(node.left), 0)
            rightsum = max(maxpath(node.right), 0)

            # update the maximum path sum
            self.maxi = max(self.maxi, leftsum + rightsum + node.val)

            return node.val + max(leftsum, rightsum)

        self.maxi = float('-inf')  # moved maxi here as a class variable
        maxpath(root)
        return self.maxi
