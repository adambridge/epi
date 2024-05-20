
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

    Invalid - fails 3rd example

    #>>> my_check_bst(Node(5, Node(3), Node(7)))
    #True
    #>>> my_check_bst(Node(5, Node(6), Node(7)))
    #False
    #>>> my_check_bst(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    #False
    """
    if not tree:
        return True
    elif tree.left and tree.left.data > tree.data:
        return False
    elif tree.right and tree.right.data < tree.data:
        return False
    else:
        return my_check_bst(tree.left) and my_check_bst(tree.right)


def book_check_bst1(tree):
    """
    Simple but inefficient method: check max left <= data and max right >= data
    My attempt for practice (could be prettier?)

    Also invalid, need to check max of l/r tree is </> data for every subtree
    therefore below fails 4th example

    #>>> book_check_bst1(Node(5, Node(3), Node(7)))
    #True
    #>>> book_check_bst1(Node(5, Node(6), Node(7)))
    #False
    #>>> book_check_bst1(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    #False
    #>>> book_check_bst1(Node(5, Node(3, Node(1), Node(2)), Node(7)))
    #False
    """
    def tree_max(tree):
        if not tree.left and not tree.right:
            return tree.data
        elif not tree.right:
            return max([tree.data, tree_max(tree.left)])
        elif not tree.left:
            return max([tree.data, tree_max(tree.right)])
        else:
            return max([tree.data, tree_max(tree.left), tree_max(tree.right)])

    if not tree:
        return True
    else:
        return ((not tree.left or tree_max(tree.left) <= tree.data)
                and (not tree.right or tree_max(tree.right) >= tree.data))


def book_check_bst1a(tree):
    """
    Second attempt at simple but inefficient method
    Still ugly and inefficent but hopefully now correct

    *Still wrong* - need to check max of left <= data and *min* of right >= data
    5th example fails

    #>>> book_check_bst1a(Node(5, Node(3), Node(7)))
    #True
    #>>> book_check_bst1a(Node(5, Node(6), Node(7)))
    #False
    #>>> book_check_bst1a(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    #False
    #>>> book_check_bst1a(Node(5, Node(3, Node(1), Node(2)), Node(7)))
    #False
    #>>> book_check_bst1a(Node(5, Node(3), Node(7, Node(4))))
    #False
    """
    def tree_max(tree):
        if not tree.left and not tree.right:
            return tree.data
        elif not tree.right:
            return max([tree.data, tree_max(tree.left)])
        elif not tree.left:
            return max([tree.data, tree_max(tree.right)])
        else:
            return max([tree.data, tree_max(tree.left), tree_max(tree.right)])

    if not tree:
        return True
    else:
        return ((not tree.left or tree_max(tree.left) <= tree.data)
                and (not tree.right or tree_max(tree.right) >= tree.data)
                and book_check_bst1a(tree.left) and book_check_bst1a(tree.right))


def book_check_bst1b(tree):
    """
    Third time lucky at simple but inefficient method?

    >>> book_check_bst1b(Node(5, Node(3), Node(7)))
    True
    >>> book_check_bst1b(Node(5, Node(6), Node(7)))
    False
    >>> book_check_bst1b(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    False
    >>> book_check_bst1b(Node(5, Node(3, Node(1), Node(2)), Node(7)))
    False
    >>> book_check_bst1b(Node(5, Node(3), Node(7, Node(4))))
    False
    """
    def aggregate_tree(tree, fn):
        if not tree:
            return tree
        else:
            return fn([agg for agg in [tree.data,
                                       aggregate_tree(tree.left, fn),
                                       aggregate_tree(tree.right, fn)] if agg is not None])

    if not tree:
        return True
    else:
        return ((not tree.left or aggregate_tree(tree.left, max) <= tree.data)
                and (not tree.right or aggregate_tree(tree.right, min) >= tree.data)
                and book_check_bst1b(tree.left) and book_check_bst1b(tree.right))


