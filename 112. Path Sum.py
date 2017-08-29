# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode(object):
    def __int__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        self.result = []
        read_list = [root.val]
        self.dfs(root, read_list)

        # print self.result


        if sum in self.result:
            return True
        else:
            return False

    def dfs(self, treenode, read_list):
        if treenode.left:
            self.dfs(treenode.left, read_list[:] + [treenode.left.val])
        if treenode.right:
            self.dfs(treenode.right, read_list[:] + [treenode.right.val])
        # print read_list
        if treenode.left == None and treenode.right == None:
            self.result.append(sum(read_list))
