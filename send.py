import socket
def send():
  buffer = 2048
  target = input('Enter Host: ')
  port = 4444
  m = input()
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target, port))
  s.listen(1)
  client, address = s.accept()
  print(address, "Has Connected.")
  
  client.send(m.encode())
  
  client.close()

send()