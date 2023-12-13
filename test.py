import tictactoe as ttt

board = ttt.initial_state()

if ttt.terminal(board):
  print("true")
else:
  print("False")


print(ttt.actions(board))
print(ttt.winner(board))