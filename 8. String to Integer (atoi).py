class node:
    def __init__(self, x):
        self.val = x
        self.next = None


import copy

a = node(1)
h = copy.copy(a)
print(a.val)
a.val = 222
print(h.val)
