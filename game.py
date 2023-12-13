import tictactoe as ttt
import re

X = "X"
O = "O"
EMPTY = ' '

class Game:
  def __init__(self, client_socket):
    self.client_socket = client_socket
    self.board = ttt.initial_state()
    self.player_mark = ''
    self.ai_mark = ''
    
  def receive(self, message):
    self.client_socket.send(message.encode())
    return self.client_socket.recv(1024).decode()

  def send(self, message):
    self.client_socket.send(message.encode())

  def print_board(self):
    board = ''
    size = len(self.board)
    for i in range(size):
      board += (" " + " | ".join(self.board[i]))
      board += ("\n")
      if i < size - 1:
          board += ("-" * (4 * size - 1))
      board += ("\n")
    return board
          


  def play(self):
    message = "Welcome to Tic Tac Toe!\nPlease choose between X or O\n"
    message += "Write 'X' or 'O' to choose player\n"

    while True:
      self.player_mark = self.receive(message).upper().strip()
      if self.player_mark != X and self.player_mark != O:
        message = "Wrong input\nPlease choose between 'X' or 'O'"
      else:
        break
    
    if self.player_mark == X:
      self.ai_mark = O
    else: 
      self.ai_mark = X


    message = "Game starts!\n"
    message += f"player: {self.player_mark}    bot: {self.ai_mark}\n"
    message += self.print_board()
    message += "\nPress Enter to continue\n"
    self.receive(message)

    while True:
      if ttt.terminal(self.board):
        break

      if ttt.player(self.board) == self.player_mark:
        message = f"Player {self.player_mark} turn!\n"
        message += f"Please enter your move in format: (i,j)\n"

        action = self.receive(message)
        while self.action_handler(action):
          message = "Wrong action!\nPlease enter your move in format: (i,j)\n"
          action = self.receive(message)

        message = "\n" + self.print_board() + "\n"
        message += "Press Enter to continue\n\n"
        self.receive(message)

      else:
        message = (f"Player {self.ai_mark} turn!\n")
        action = ttt.minimax(self.board)
        self.board = ttt.result(self.board, action)
        message += (self.print_board()) + "\n"
        message += "Press Enter to continue\n"
        self.receive(message)

    winner = ttt.winner(self.board)
    if winner:
      self.send(f"Player {ttt.winner(self.board)} wins!\n")
    else:
      self.send("It's a tie!\n")


  def action_handler(self, action):
    action = action.strip()
    if len(action) != 5:
      return True
    regex = "\([0-2],[0-2]\)"
    if not re.search(regex, action):
      return True
    action = [int(action[1]), int(action[3])]
    
    try:
      self.board = ttt.result(self.board, action)
    except:
      return True
    
    return False


    

    
