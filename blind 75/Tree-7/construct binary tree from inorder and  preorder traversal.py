# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i]==root.val:
                root.left = self.buildTree(preorder[1:i+1],inorder[:i])
                root.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return root
    

#using hashmap for indexes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Build a hashmap for inorder values to index
        self.inorder_index = {}
        for i in range(len(inorder)):
            self.inorder_index[inorder[i]] = i

        return self._build(preorder, inorder)

    def _build(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        idx = self.inorder_index[root.val]  # O(1) lookup

        root.left = self._build(preorder[1:1+idx], inorder[:idx])
        root.right = self._build(preorder[1+idx:], inorder[idx+1:])
        return root
