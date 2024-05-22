
"""
Value of element is width of disc
Last element is top of tower
Refer to towers by index: 0, 1, 2
Print sequence to move discs from 0 to 1

examples:

  0    1  2
((2,1),(),())   target: 1
((2),(),(1))
((),(2),(1))
((),(2,1),())

((3,2,1),(),())
((3,2),(1),())
((3),(1),(2))
((3),(),(2,1))
((),(3),(2,1))
((1),(3),(2))
((1),(3,2),())
((),(3,2,1),())

General pattern for n rings:
1. move n - 1 rings to intermediary (i.e. peg that is not target) using target as intermediary
2. move nth ring to target
3. move n - 1 rings to target from intermediary

-> 1 and 3 can each be individually permormed using this pattern -> recursion
"""


def list_moves(towers, n, fro, to, via):
    """
    My reimplementation of book solution 
    >>> list_moves([[2,1],[],[]], 2, 0, 1, 2)
    [[0, 2], [0, 1], [2, 1]]
    """

    def move_rings(n, fro, to, via):
        if n > 0:
            move_rings(n - 1, fro, via, to)
            towers[to].append(towers[fro].pop())
            moves.append([fro, to])
            move_rings(n - 1, via, to, fro)

    moves = []
    move_rings(n, fro, to, via)
    return moves


