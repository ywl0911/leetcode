class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


l = []


def caluate_deepth(root, i):
    if root.left:
        caluate_deepth(root.left, i + 1)
    if root.right:
        caluate_deepth(root.right, i + 1)
    l.append(i)

t=[]
for i in range(10):
    t.append(TreeNode(i))

t[1].left=t[2]
t[1].right=t[3]
t[2].left=t[4]


caluate_deepth(t[1],1)
print l

