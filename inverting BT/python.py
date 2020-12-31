class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        

def invertBinaryTree(tree: TreeNode):
    temp = tree.left 
    tree.left = tree.right
    tree.right = temp
    invertBinaryTree(tree.right)
    invertBinaryTree(tree.left)
