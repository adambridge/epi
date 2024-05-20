
class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.data}, {self.left}, {self.right})"


def my_check_bst(tree):
    """
    Check that tree conforms to the BST property
    """
    if not tree:
        return True
    elif tree.left and tree.left.data > tree.data:
        return False
    elif tree.right and tree.right.data < tree.data:
        return False
    else:
        return my_check_bst(tree.left) and my_check_bst(tree.right)

