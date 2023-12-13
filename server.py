import socket
import threading

import game


def main():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('localhost', 4444))
  server_socket.listen(100)

  print("Server started working\nServer port: 4444")

  while True:
    try: 
      client_socket, address = server_socket.accept()
    except:
      print("\nServer stopped working")
      server_socket.close()
      break
    print("connected: ", address)

    client_thread = threading.Thread(target = handle_client, args=(client_socket, address))
    client_thread.start()

def handle_client(client_socket, address):

  try:
    game.Game(client_socket).play()
  except:
    pass
  finally:
    print(f"disconnected: ", address)
  client_socket.close()

if __name__ == '__main__':
  main()