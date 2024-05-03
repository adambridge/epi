
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        if self.next:
            return f"{self.data}-{self.next}"
        else:
            return f"{self.data}"


def my_recursive_merge(l1, l2):
    """
    Merge two linked lists, first attempt
    Could be recursive like Node(head.data, merge(other, tail)
    or creating no new nodes (just rearranging)
    can have recursive without creating new Nodes?

    l1: 1-2-3
    l2: 4-5-6

    1 will be new head, tail will be merge of 2-3 and 4-5-6

    >>> l1 = Node(1, Node(3, Node(6)))
    >>> l2 = Node(2, Node(4, Node(5)))
    >>> my_recursive_merge(l1, l2)
    1-2-3-4-5-6
    """
    if l1 is None or l2 is None:
        return l1 or l2
    
    if l1.data > l2.data:
        head = l2
        other = l1
    else:
        head = l1
        other = l2

    head.next = my_recursive_merge(head.next, other)
    return head


