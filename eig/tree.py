class node:
    def __init__(self, n, value=None, label=[]):
        self.value = value                      # current node value
        self.label = label                      # current node label
        self.child = [None for i in range(n)]   # list of children
        self.chcount = 0                        # no. of active children

    # creates a child for current node
    def adopt(self, node):
        if self.chcount < len(self.child):
            self.child[self.chcount] = node
            self.chcount += 1

# prints the tree by dfs
def show(root, level=0):
    if root.chcount > 0:
        print(('  ')*level, root.value, root.label)
        for i in range(root.chcount):
            show(root.child[i], level+1)
    else:
        print('  '*level, root.value, root.label)

# finds node by dfs
def find(root, label):
    if root.label == label:
        return root
    if root.chcount > 0:
        for i in range(root.chcount):
            x = find(root.child[i], label)
            if x != None:
                return x
    return None
