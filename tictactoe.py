"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = ' '


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
    num_x = 0
    num_o = 0
    for row in board:
      for cell in row:
        if cell == X:
          num_x += 1
        if cell == O:
          num_o += 1
    if num_x == 0 and num_o == 0 or num_x == num_o:
      return X
    else:
      return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          actions.append((i, j))
    return set(actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
      raise Exception
    current_player = player(board)
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = current_player
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    empty_board = initial_state()
    if empty_board == board:
      return None

    for row in board:
      if row[0] == row[1] and row[1] == row[2] and row[0] != EMPTY:
        return row[0]
    
    for i in range(3):
      if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != EMPTY:
        return board[0][i]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
      return board[1][1]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
      return board[1][1]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) or len(actions(board)) == 0:
      return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
      return 1
    elif winner(board) == O:
      return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
      return None
    
    rated_moves = {}
    current_player = player(board)
    acts = actions(board)
    for action in acts:
      
      new_board = result(board, action)
      if current_player == X:
        rated_moves[action] = min_value(new_board)
      else:
        rated_moves[action] = max_value(new_board)
    if current_player == X:
      return max_random_action(rated_moves)
    else:
      return min_random_action(rated_moves)

def max_value(board):
  if terminal(board):
    return utility(board)
  v = -1
  for action in actions(board):
    v = max(v, min_value(result(board, action)))
    if v == 1:
      return v
  return v

def min_value(board):
  if terminal(board):
    return utility(board)
  v = 1
  for action in actions(board):
    v = min(v, max_value(result(board, action)))
    if v == -1:
      return v
  return v

def min_random_action(rated_actions):
  min_v = min(rated_actions.values())
  return random.choice([key for key in rated_actions if rated_actions[key] == min_v])

def max_random_action(rated_actions):
  max_v = max(rated_actions.values())
  return random.choice([key for key in rated_actions if rated_actions[key] == max_v])
