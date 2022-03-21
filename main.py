import sys
import socket
if len (sys.argv) >= 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print('invalid argument')

#print(str(sys.argv))
#protocol = str(sys.argv[2])
#print(protocol)

def server():
  import socket            
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
    client.send('THIS IS A TEST'.encode())
    client.close()
    break
  
def client():
  import socket            
  s = socket.socket()        
  port = 4444               
  s.connect(('127.0.0.1', port))
  print (s.recv(1024).decode())
  s.close()


def Tcp_Scanner(target):
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#a = socket.socket()
		socket.setdefaulttimeout(1)
		output = s.connect_ex((target,port))
		if output == 0:
			#a.connect((target, int(port)))
			print("open: {}".format(port))
			#print(a.recv(1024)
		s.close()



try:
	#creating an if statement for a future feature where 
	#The program is able to select between different features
	#Based on user Input
  print('Select 1 for scanner')
  print('Select 2 for server')
  print('Select 3 for client')
  choice = int(input('> '))
  if choice == 1:
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