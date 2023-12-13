import socket

def main():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(('localhost', 4444))

  while True:
    message = client_socket.recv(1024).decode()
    print(message)

    if "wins" in message:
      break

    try:
      action = input()
      if not action:
        action = ":>"
      client_socket.send(action.encode())
    except:
      break
  
  client_socket.close()

if __name__ == '__main__':
    main()