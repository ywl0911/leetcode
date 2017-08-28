# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.l = []
        self.bianli(root)
        return self.l

    def bianli(self, root):
        if root == None:
            return
        if root.left:
            self.bianli(root.left)
        self.l.append(root.val)
        if root.right:
            self.bianli(root.right)
