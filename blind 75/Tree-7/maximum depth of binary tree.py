class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        if not root.left: #bcz if one subtree misses we need to consideer another subtree,you can also not mention this
            return 1+self.maxDepth(root.right)
        if not root.right:
            return 1+self.maxDepth(root.left)
        
        left_depth = self.maxDepth(root.left) #if left and right subtrees exists
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
