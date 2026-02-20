"""
Tic Tac Toe Player
"""

import math
import copy

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
    # Count X and O
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # X goes first
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid move")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Rows
    for row in board:
        if row == [X, X, X]:
            return X
        if row == [O, O, O]:
            return O

    # Columns
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col == [X, X, X]:
            return X
        if col == [O, O, O]:
            return O

    # Diagonals
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]

    if diag1 == [X, X, X] or diag2 == [X, X, X]:
        return X
    if diag1 == [O, O, O] or diag2 == [O, O, O]:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # Check if board full
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current = player(board)

    # If AI is X → maximize
    if current == X:
        best_value = -math.inf
        best_move = None

        for move in actions(board):
            value = min_value(result(board, move))
            if value > best_value:
                best_value = value
                best_move = move

        return best_move

    # If AI is O → minimize
    else:
        best_value = math.inf
        best_move = None

        for move in actions(board):
            value = max_value(result(board, move))
            if value < best_value:
                best_value = value
                best_move = move

        return best_move


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v

