class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.data}, {self.left}, {self.right})"

def my_search_bst(node, key):
    """
    my grug brained version
    """
    if node.data == key:
        return node
    elif node.left and key < node.data:
        return search_bst(node.left, key)
    elif node.right and key > node.data:
        return search_bst(node.right, key)
    else:
        return None

def book_search_bst(tree, key):
    """
    cool chad book version with nested ternary flex
    """
    return (tree
            if not tree or tree.data == key
            else book_search_bst(tree.left, key) if key < tree.data
            else book_search_bst(tree.right, key))
