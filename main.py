import sys
import socket
if len (sys.argv) >= 2:
	target = socket.gethostbyname(sys.argv[1])
	#print(target)
else:
	print('invalid argument')

#protocol = sys.argv[2]

for port in range(1,65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	output = s.connect_ex((target,port))
	if output == 0:
		print("open: {}".format(port))
	s.close()

#if protocol == 't':
#	for port in range(1,65535):
#		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#		socket.setdefaulttimeout(1)
#		output = s.connect_ex((target,port))
#		if output == 0:
#			print("open: {}".format(port))
#		s.close()
#elif protocol == 'u':
#	for port in range(1,65535):
#		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#		socket.setdefaulttimeout(1)
#		output = s.connect_ex((target,port))
#		if output == 0:
#			print("open: {}".format(port))
#		s.close()
