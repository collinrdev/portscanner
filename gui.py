#imports
import sys
import socket
from tkinter import *
from tkinter import ttk

#create root window
root = Tk()
#Create title
root.title("Port Scanner")

#Create Tab Control
tabControl = ttk.Notebook(root)
#Create Tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
#Pack Tabs
tabControl.add(tab1, text ='Scanner')
tabControl.add(tab2, text ='Server')
tabControl.add(tab3, text ='Client')
tabControl.pack(expand=1, fill="both")

#Create labels and set atrributes
#Scanner
label1 = ttk.Label(tab1, text = "Enter IP: ")
label1.grid()
label3 = ttk.Label(tab1, text = "Open Ports:")
label3.grid()
label2 = ttk.Label(tab1, text = "")
label2.grid()
#Scanner entry field
ip = ttk.Entry(tab1, width=10)
ip.grid(column =1, row =0)

#Server
serverPort = ttk.Entry(tab2, width=10)
serverPort.grid(column=1,row=0)
serverMessage = ttk.Entry(tab2, width=10)
serverMessage.grid(column=1,row=1)
portLabel = ttk.Label(tab2, text = "Enter Port: ")
portLabel.grid(column=0,row=0)
message = ttk.Label(tab2, text = "Enter Message: ")
message.grid(column=0,row=1)
serveroutput = ttk.Label(tab2, text = "output")
serveroutput.grid(column=0,row=2)
#Client
clientPortEntry = ttk.Entry(tab3, width=10)
clientPortEntry.grid(column=1,row=0)
clientIPEntry = ttk.Entry(tab3, width=10)
clientIPEntry.grid(column=1,row=1)
clientPort = ttk.Label(tab3, text = "Enter Port: ")
clientPort.grid(column=0,row=0)
clientIP = ttk.Label(tab3, text = "Enter IP: ")
clientIP.grid(column=0,row=1)
clientOutput = ttk.Label(tab3, text = "")
clientOutput.grid()

#Portscanner function
def scanner():
        target = ip.get()
        portlist = []
        for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                output = s.connect_ex((target,port))
                if output == 0:
                        portlist.append(port)
                s.close()
        label2.configure(text = portlist)

#Server Function
def server():
  message = serverMessage.get()
  port = int(serverPort.get())
  s = socket.socket()        
  print('Socket started')
  #serverPort = int(input("Enter port: "))               
  s.bind(('', port))        
  print('binded to port: %s' %(port))
  s.listen(5)    
  print('Listening...')           
  while True:   
    client, address = s.accept()    
    print('Connection From: ', address )
    serveroutput.configure(text = address)
    client.send(message.encode())
    client.close()
    break
  
#Client Function
def client():            
  s = socket.socket()        
  port = int(clientPortEntry.get())
  ip = clientIPEntry.get()
  s.connect((ip, port))
  message = s.recv(1024).decode()
  clientOutput.configure(text = message)
  s.close()

#button to start scan
btn = ttk.Button(tab1, text = "Scan", command=scanner)
btn.grid(column=2, row=0)
#Server Button
serverStart = ttk.Button(tab2, text="Start", command=server)
serverStart.grid(column=2,row=0)
#Client Button
clientStart = ttk.Button(tab3, text="Start", command=client)
clientStart.grid(column=2,row=0)
#run the program
root.mainloop()