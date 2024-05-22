
# initial configuration:
towers = ((6,5,4,3,2,1),(),())

"""
Value of element is width of disc
Last element is top of tower
Refer to towers by index: 0, 1, 2
Print sequence to move discs from 0 to 1

examples:

((3,2,1),(),())

((3,2,1),(),()) cpdiip
((3,2),(1),())  cpdiip
((3),(1),(2))   cpdiip
((3),(),(2,1))
((),(3),(2,1))  cpdiip
((1),(3),(2))
((1),(3,2),())
((),(3,2,1),())



((6,5,4,3,2,1),(),())
"""

def moves(start, end):
    """
    Return (shortest?) sequence of moves to get from start configuration to end
    Sequence ((0,1),(1,0)) means move top disc from tower 0 to 1 then back from 1 to 0
    
    Base case is when end is one move away from start

    if "one move away":
        return "that one move"
    else:
        return "moves(1, n-1)" + "last move"

    #>>> moves(((1),()), ((),(1)))
    #((0,1))
    """
    final_move = one_off(start, end)
    if len(final_move) != 0:
        return (final_move)
    else:
        prev, move = rewind(end, start)
        return moves(start, prev_end) + (move,)


def one_off(start, end):
    """
    Answers the question, is start one move off end? If so return that move.

    Iterate start and end towers, as soon as have two where start and end are not equal
    check if moving from one that starts taller to on that starts shorter results in
    correct end state and return move if so otherwise return None
    >>> one_off(((1,), (3, 2)), ((), (3, 2, 1)))
    (0, 1)
    >>> one_off(((3, 2, 1), ()), ((), (3, 2, 1)))
    """
    changed = ()
    for i in range(len(end)):
        if len(end[i]) != len(start[i]):
            changed = changed + (i,)
        if len(changed) > 1:
            break

    if len(changed) < 2:
        None

    if len(start[changed[0]]) > len(end[changed[0]]):
        fro, to = changed[0], changed[1]
    else:
        fro, to = changed[1], changed[0]

    if start[fro][-1] == end[to][-1] \
            and start[fro][:-1] == end[fro] \
            and start[to] == end[to][:-1]:
        return (fro, to)


def can_put_disc_in_initial_position(start, end):
    """
    From position end, is there a single move that puts a disc in it's correct starting position
    as defined by start? If so return a tuple: (state with disc replaced, move to replace disc)
    otherwise return None 

    Iterate through start rings, if end has same ring in same position, look at next. 
    If end doesn't have that ring, check if it's available on top of another stack, if it is
    then that is the move returned.
    >>> can_put_disc_in_initial_position(((3, 2, 1), (), ()), ((3,), (1,), (2,)))
    (((3, 2), (1,), ()), (2, 0))
    """
    for tower in range(len(start)):
        for i in range(len(start[tower])):
            if len(end[tower]) > i and end[tower] == start[tower]:
                next
            if len(end[tower]) == i:
                fro = is_accessible(start[tower][i], end)
                if fro:
                    move = (fro, tower)
                    break
        if move:
            break
    if move:
        return (apply(move, end), move)


def is_accessible(disc, state):
    """
    Is disc accessible, i.e. on top of a tower in the given state?
    If so return the index of the tower it's on.
    """
    for tower in range(len(state)):
        if state[tower][-1] == disc:
            return tower


def apply(move, state):
    """
    >>> apply((3, 1), ((7, 1), (6,), (5,), (4, 2), (3,)))
    ((7, 1), (6, 2), (5,), (4,), (3,))
    """
    fro, to = move
    disc = state[fro][-1]
    if to < fro:
        return state[:to] + (state[to] + (disc,),) + state[to + 1:fro] \
            + (state[fro][:-1],) + state[fro + 1:]
    else:
        return state[:fro] + (state[fro][:-1],) + state[fro + 1:to] \
            + (state[to] + (disc,),) + state[to + 1:]


def rewind(end, start):
    """
    Go back one move from end state towards start returning previous state and subsequent move
    """
    move = one_off(start, end)
    if len(move) != 0:
        return start, move

    state, move = can_put_disc_in_initial_position(start, end)
    if len(move) != 0:
        return state, move

