import sys
import socket


#if len (sys.argv) >= 2:
#	target = socket.gethostbyname(sys.argv[1])
#else:
#	print('invalid argument')


#print(str(sys.argv))
#protocol = str(sys.argv[2])
#print(protocol)

# Server to send message
def server():
  message = input('Type your Message: ')
  s = socket.socket()        
  print ('Socket started')
  port = 4444               
  s.bind(('', port))        
  print ('binded to port: %s' %(port))
  s.listen(5)    
  print ('Listening...')           
  while True:   
    client, address = s.accept()    
    print ('Connection From: ', address )
    client.send(message.encode())
    client.close()
    break

# Client to recieve message
def client():            
  s = socket.socket()        
  port = 4444               
  s.connect(('127.0.0.1', port))
  print (s.recv(1024).decode())
  s.close()

# Scanner
def Tcp_Scanner(target):
  for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#a = socket.socket()
    socket.setdefaulttimeout(1)
    output = s.connect_ex((target,port))
    if output == 0:
      #a.connect((target, int(port)))
      if port == 22:
        print("open: {} SSH".format(port))
      elif port == 80:
        print("open: {} HTTP".format(port))
      elif port == 53:
        print("open: {} DNS".format(port))
      elif port == 20:
        print("open: {} FTP".format(port))
      elif port == 21:
        print("open: {} FTP".format(port))
      elif port == 25:
        print("open: {} SMTP".format(port))
      elif port == 110:
        print("open: {} POP3".format(port))
      elif port == 123:
        print("open: {} NTP".format(port))
      elif port == 143:
        print("open: {} IMAP".format(port))
      elif port == 161:
        print("open: {} SNMP".format(port))
      elif port == 194:
        print("open: {} IRC".format(port))
      elif port == 443:
        print("open: {} HTTPS".format(port))
      else:
        print("open: {}".format(port))
			#print(a.recv(1024)
    s.close()

#Try and accept loop for error handling and choosing which function to run
try:
  print('Please Select an Option...')
  print('1) for scanner')
  print('2) for server')
  print('3) for client')
  choice = int(input('> '))
  if choice == 1:
    target = input("Enter Target: ")
    target = socket.gethostbyname(target)
    Tcp_Scanner(target)
  elif choice == 2:
    server()
  elif choice == 3:
    client()
  else:
	  sys.exit()
except KeyboardInterrupt:
	print('Program interrupted!')
	sys.exit()
except socket.error:
	print('No Response!')
	sys.exit()
except socket.gaierror:
	print('Bad Hostname!')
	sys.exit()
