class Tree(object):
    def __init__(self,val):
        self.right=None
        self.left=None
        self.value=val
root=Tree(8)
root.left=Tree(4)
root.left.left=Tree(2)
root.left.right=Tree(6)
root.right=Tree(10)
root.right.right=Tree(20)
root.right.right.right=Tree(34)
root.right.right.right.left=Tree(24)


# Implement a function to check if a tree is balanced
# For the purposes of this question, a balanced tree is defined to be a tree
# such that no two leaf nodes differ in distance from the root by more than one
def balancedTree(Tree):
    if Tree is None:
        return True
    def get_height(t):
        if t is None:
            return 0
        return 1+max(get_height(t.left),get_height(t.right))
    return abs(get_height(Tree.left)-get_height(Tree.right))<=1

print(balancedTree(root))