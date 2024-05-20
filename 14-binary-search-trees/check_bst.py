from functools import cache
from numpy import inf

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

    Invalid - fails 3rd example since only checks immediate children, not all descendents

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


def simple_check_bst1(tree):
    """
    Simple but inefficient method: check max left <= data and max right >= data
    My attempt for practice

    Also invalid, need to check max of l/r tree is </> data for every subtree
    therefore below fails 4th example

    #>>> simple_check_bst1(Node(5, Node(3), Node(7)))
    #True
    #>>> simple_check_bst1(Node(5, Node(6), Node(7)))
    #False
    #>>> simple_check_bst1(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    #False
    #>>> simple_check_bst1(Node(5, Node(3, Node(1), Node(2)), Node(7)))
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


def simple_check_bst2(tree):
    """
    Second attempt at simple but inefficient method
    Still ugly and inefficent but hopefully now correct

    *Still wrong* - need to check max of left <= data and *min* of right >= data
    5th example fails

    #>>> simple_check_bst2(Node(5, Node(3), Node(7)))
    #True
    #>>> simple_check_bst2(Node(5, Node(6), Node(7)))
    #False
    #>>> simple_check_bst2(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    #False
    #>>> simple_check_bst2(Node(5, Node(3, Node(1), Node(2)), Node(7)))
    #False
    #>>> simple_check_bst2(Node(5, Node(3), Node(7, Node(4))))
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
                and simple_check_bst2(tree.left) and book_check_bst1a(tree.right))


def simple_check_bst3(tree):
    """
    Third time lucky at simple but inefficient method
    Worst case O(n^2) though caching (functools.cache) gets O(n) at cost O(n) memory

    >>> simple_check_bst3(Node(5, Node(3), Node(7)))
    True
    >>> simple_check_bst3(Node(5, Node(6), Node(7)))
    False
    >>> simple_check_bst3(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    False
    >>> simple_check_bst3(Node(5, Node(3, Node(1), Node(2)), Node(7)))
    False
    >>> simple_check_bst3(Node(5, Node(3), Node(7, Node(4))))
    False
    """
    @cache
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
                and simple_check_bst3(tree.left) and simple_check_bst3(tree.right))


def constraint_check_bst(tree, lower=-inf, upper=inf):
    """
    Attempt to implement more efficient bst check.
    Descend recursively accumulating constraints
    >>> constraint_check_bst(Node(5, Node(3), Node(7)))
    True
    >>> constraint_check_bst(Node(5, Node(6), Node(7)))
    False
    >>> constraint_check_bst(Node(5, Node(3, Node(1), Node(6)), Node(7)))
    False
    >>> constraint_check_bst(Node(5, Node(3, Node(1), Node(2)), Node(7)))
    False
    >>> constraint_check_bst(Node(5, Node(3), Node(7, Node(4))))
    False
    """
    if not tree:
        return True
    elif tree.data < lower or tree.data > upper:
        return False
    else:
        return (constraint_check_bst(tree.left, lower=lower, upper=min([upper, tree.data]))
                and constraint_check_bst(tree.right, lower=max([lower, tree.data]), upper=upper))


