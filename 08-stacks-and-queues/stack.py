
class Stack:
    """
    Implement a stack with push, pop, and max
    >>> s = Stack()
    >>> print("ignore"); s.push(7).push(2).push(3) # doctest:+ELLIPSIS
    ignore...
    >>> s.pop()
    3
    >>> s.pop()
    2
    >>> s.max()
    7
    """
    def __init__(self):
        self.stack = []
        self.max_stack = []


    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val > self.max():
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max())
        return self


    def pop(self):
        return self.stack.pop()


    def max(self):
        """
        Could just calculate each time, probably a better way though...
        Alternative is to keep a secondary stack with max:
        """
        return self.max_stack[-1] if self.max_stack else None

