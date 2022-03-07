#imports
import sys
import socket
from tkinter import *

#create root window
root = Tk()
#Create title
root.title("Port Scanner")

#Create labels and set atrributes
label1 = Label(root, text = "Enter IP: ")
label1.grid()
label3 = Label(root, text = "Open Ports:")
label3.grid()
label2 = Label(root, text = "", fg="green")
label2.grid()

#entry field
ip = Entry(root, width=10)
ip.grid(column =1, row =0)
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

#button to start scan
btn = Button(root, text = "Scan", fg = "red", command=scanner)
btn.grid(column=2, row=0)
#run the program
root.mainloop()