
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def height(self):
        """
        Return the hieght of this tree (my attempt before looking at book answer)
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
        >>> Tree(0, Tree(1, Tree(2))).height()
        2
        """
        # print(f"{self.data}") # check traversal order
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


    def height_balanced(self):
        """
        Return True if height difference between left and right for all trees is no more than 1
               0
           1       2
         3   4
        5               -> False

               0
           1       2
         3   4   5      -> True
        >>> Tree(0, Tree(1, Tree(3, Tree(5)), Tree(4)), Tree(2)).height_balanced()
        False
        >>> Tree(0, Tree(1, Tree(3), Tree(4)), Tree(2, Tree(5))).height_balanced()
        True
        """
        if abs(self.left.height() - self.right.height()) <= 1:
            return True
        else:
            return False


