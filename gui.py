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
#Pack Tabs
tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand=1, fill="both")

#Create labels and set atrributes
label1 = ttk.Label(tab1, text = "Enter IP: ")
label1.grid()
label3 = ttk.Label(tab1, text = "Open Ports:")
label3.grid()
label2 = ttk.Label(tab1, text = "")
label2.grid()

#entry field
ip = ttk.Entry(tab1, width=10)
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
btn = ttk.Button(tab1, text = "Scan", command=scanner)
btn.grid(column=2, row=0)
#run the program
root.mainloop()