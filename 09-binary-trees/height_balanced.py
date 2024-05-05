
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def height(self):
        """
        Return the hieght of this tree
        >>> Tree(0, Tree(1, Tree(2))).height()
        2
        """
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



