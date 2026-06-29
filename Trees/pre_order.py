class binary_Tree:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


def pre_order(Root):
        if Root==None: return
        print(Root.value)
        pre_order(Root.left)
        pre_order(Root.right)


Root=binary_Tree(1)
node1=binary_Tree(2)
node2=binary_Tree(3)
node3=binary_Tree(4)
node4=binary_Tree(5)
node5=binary_Tree(6)

Root.left=node2
Root.left=node4

node2.right=node3
node2.right=node5

pre_order(Root)