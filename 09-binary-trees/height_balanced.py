from collections import namedtuple

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def height(self):
        """
        Return the hieght of this tree (my attempt before looking at book answer)
        >>> Tree(0, Tree(1, Tree(2))).height()
        2
        """
        # print(f"height visited node {self.data}") # check traversal order
        if self.left is None:
            if self.right is None:
                return 0
            else:
                return self.right.height() + 1
        else:
            if self.right is None:
                return self.left.height() + 1
            else:
                return max([self.left.height(), self.right.height()]) + 1


    def height_balanced_borked(self):
        """
        Return True if height difference between left and right for all trees is no more than 1
        Thoughts after comparing with book answer:
        - Not a correct solution since it only compares the heights of left and right from root,
          should recursively check if height balanced from all nodes.
        - Is this inorder, preorder, postorder or something else?
            Not obvious but could add print to check -> preorder
        - Would this benefit from a cache? Only visits each node once.
        - Book solution can apparently terminate early. How?
            If left subtree is not balanced no need to check right.
            Can this be done in my version?
        - What is time complexity? space complexity is O(h) due to stack (h = height of tree)
            Think time is O(n) for n nodes.
        - Making height not an instance method means can have single `if tree` check
          mine has to check left and right.

               0
           1       2
         3       4
        5               -> False (Fails)

               0
           1       2
         3   4
        5               -> False

               0
           1       2
         3   4   5      -> True

        #>>> Tree(0, Tree(1, Tree(3, Tree(5))), Tree(2, Tree(4))).height_balanced_borked()
        False -> returns True, fails to notice that l is not balanced
        >>> Tree(0, Tree(1, Tree(3, Tree(5)), Tree(4)), Tree(2)).height_balanced_borked()
        False
        >>> Tree(0, Tree(1, Tree(3), Tree(4)), Tree(2, Tree(5))).height_balanced_borked()
        True
        """
        if abs(self.left.height() - self.right.height()) <= 1:
            return True
        else:
            return False


    def height_balanced(self):
        """
        height balanced if abs(h(l) - h(r)) <= 1 and hb(l) and hb(r)
        - This version does check every node but have very similar recursion logic in height
          and height_balanced
        - Still inefficient from having separate recursions for height and balance

        >>> Tree(0, Tree(1, Tree(3, Tree(5))), Tree(2, Tree(4))).height_balanced()
        False
        >>> Tree(0, Tree(1, Tree(3, Tree(5)), Tree(4)), Tree(2)).height_balanced()
        False
        >>> Tree(0, Tree(1, Tree(3), Tree(4)), Tree(2, Tree(5))).height_balanced()
        True
        """
        # print(f"height_balanced visited node {self.data}")
        if not self.left:
            if not self.right:
                return True
            else:
                # if no left tree, height of right cannot be more than 1 but regular height
                # function will keep going. Hmm. Could have height_less_than()? For now:
                return self.right.height_balanced() and self.right.height() < 1
        else:
            if not self.right:
                return self.left.height_balanced() and self.left.height() < 1
            else:
                return self.left.height_balanced() and self.right.height_balanced() \
                and abs(self.left.height() - self.right.height()) < 1


def is_balanced(tree):
    """
    reimplement after reading book solution
    recursive fn return named tuple with height and balanced-ness wrapped in a function that
    return balanced-ness

    >>> is_balanced(Tree(0, Tree(1, Tree(3, Tree(5))), Tree(2, Tree(4))))
    False
    >>> is_balanced(Tree(0, Tree(1, Tree(3, Tree(5)), Tree(4)), Tree(2)))
    False
    >>> is_balanced(Tree(0, Tree(1, Tree(3), Tree(4)), Tree(2, Tree(5))))
    True
    """
    HeightAndBalance = namedtuple('HeightAndBalance', ('height', 'balanced'))

    def height_and_balance(tree):
        if not tree:
            # height of parent is height of child +1 -> parent with 2 None children is 0
            return HeightAndBalance(-1, True)
        # print(f"hab {tree.data}")

        left_hb = height_and_balance(tree.left)
        if not left_hb.balanced:
            return HeightAndBalance(-1, False) # -1 meaning didn't bother calculating height

        right_hb = height_and_balance(tree.right)
        if not right_hb.balanced:
            return HeightAndBalance(-1, False)

        height = max([left_hb.height, right_hb.height]) + 1
        balanced = abs(left_hb.height - right_hb.height) <= 1
        return HeightAndBalance(height, balanced)

    return height_and_balance(tree).balanced


