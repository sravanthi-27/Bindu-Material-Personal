import collections
class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root:Treenode):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)            
            if level:
                res.append(level)
        return res
root = Treenode(1,
        Treenode(2, Treenode(4), Treenode(5)),
        Treenode(3))

sol = Solution()
print(sol.levelOrder(root))  # Output: [[1], [2, 3], [4, 5]]