"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    def count():
        x_count, o_count = 0, 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == X:
                    x_count += 1
                elif board[row][col] == O:
                    o_count += 1
    
        return x_count, o_count
    
    x_count, o_count = count()
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    def identify_empty():
        empty_coords = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == EMPTY:
                    empty_coords.add((row, col))
    
        return empty_coords
    return identify_empty()


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action[0], action[1]
    if not (0 <= row <= 2 and 0 <= col <= 2):
        raise ValueError("Action's row col value out of bound")
    elif board[row][col] != EMPTY:
        raise ValueError("Action's destination cell already contains a player's move")

    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check horizontal winner
    for row in range(len(board)):
        first_elem = board[row][0]
        win = True
        for col in range(len(board[row])):
            if first_elem != board[row][col]:
                win = False
        
        if win == True and first_elem != EMPTY:
            return first_elem
    
    # check vertical winner
    for col in range(len(board)):
        first_elem = board[0][col]
        win = True
        for row in range(len(board[col])):
            if first_elem != board[row][col]:
                win = False
        
        if win == True and first_elem != EMPTY:
            return first_elem

    # check diagonal winner : (0,0) (1,1) (2,2)
    first_elem = board[0][0]
    win = True
    for row in range(len(board)):
        if first_elem != board[row][row]:
            win = False
    
    if win == True and first_elem != EMPTY:
        return first_elem

    # check diagonal winner : (0,2) (1,1) (2,0)
    first_elem = board[0][2]
    win = True
    for row in range(len(board)):
        if first_elem != board[row][(len(board) - 1) - row]:
            win = False
    
    if win == True and first_elem != EMPTY:
        return first_elem
    
    # no winner found
    return None

        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_player = winner(board)

    if winner_player is not None:
        return True
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    
    # a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    
    current_player = player(board)
    actions_available = actions(board)
    current_best_action = None
    
    if current_player == X:
        current_max = -math.inf
        for action in actions_available:
            simulate = result(board=board, action=action)
            value = minmax_aux(simulate)
            if value > current_max:
                current_best_action = action
                current_max = value
    else:
        current_min = math.inf
        for action in actions_available:
            simulate = result(board=board, action=action)
            value = minmax_aux(simulate)
            if value < current_min:
                current_best_action = action
                current_min = value
    
    return current_best_action


def minmax_aux(board, alpha=-math.inf, beta=math.inf):
    if terminal(board) == True:
        return utility(board)
    
    current_player = player(board)
    actions_available = actions(board)

    if current_player == X:
        current_max = -math.inf
        for action in actions_available:
            simulate = result(board=board, action=action)
            value = minmax_aux(board=simulate, alpha=max(current_max, alpha), beta=beta)
            current_max = max(current_max, value)

            if current_max >= beta:
                break

        return current_max
    else:
        current_min = math.inf
        for action in actions_available:
            simulate = result(board=board, action=action)
            value = minmax_aux(board=simulate, alpha=alpha, beta=min(current_min, beta))
            current_min = min(current_min, value)

            if current_min <= alpha:
                break

        return current_min
