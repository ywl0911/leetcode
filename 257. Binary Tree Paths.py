# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        t: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return []
        self.result = []
        read_list = [str(root.val)]
        self.dfs(root, read_list)

        return self.result

    def dfs(self, treenode, read_list):
        if treenode.left:
            self.dfs(treenode.left, read_list[:] + [str(treenode.left.val)])
        if treenode.right:
            self.dfs(treenode.right, read_list[:] + [str(treenode.right.val)])
        # print read_list
        if treenode.left == None and treenode.right == None:
            self.result.append('->'.join(read_list))
