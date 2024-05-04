class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def inorder(self, root=True):
        """
           0
         1   2
        3 4 5 6
        >>> Tree(0, Tree(1, Tree(3), Tree(4)), Tree(2, Tree(5), Tree(6))).inorder()
        3 1 4 0 5 2 6 
        """
        if self.left:
            self.left.inorder(root=False)
        print(f"{self.data} ", end="")
        if self.right:
            self.right.inorder(root=False)
        if root:
            print()


    def preorder(self, root=True):
        """
           0
         1   2
        3 4 5 6
        >>> Tree(0, Tree(1, Tree(3), Tree(4)), Tree(2, Tree(5), Tree(6))).preorder()
        0 1 3 4 2 5 6 
        """
        print(f"{self.data} ", end="")
        if self.left:
            self.left.preorder(root=False)
        if self.right:
            self.right.preorder(root=False)
        if root:
            print()


    def postorder(self, root=True):
        """
           0
         1   2
        3 4 5 6
        >>> Tree(0, Tree(1, Tree(3), Tree(4)), Tree(2, Tree(5), Tree(6))).postorder()
        3 4 1 5 6 2 0 
        """
        if self.left:
            self.left.postorder(root=False)
        if self.right:
            self.right.postorder(root=False)
        print(f"{self.data} ", end="")
        if root:
            print()


