#EITHER I CAN USE TKINTER/ QT5 /  KIVY
# import nmap
import os
import tkinter as tk
import subprocess
import logging



def set_logger(logfile):
        logfile =  logfile  # prepend path "logs/"
        loglevel = logging.INFO  # adjust as desired
        dtfmt = '%m/%d/%Y %I:%M:%S %p'
        logfmt = "%(levelname)s: %(asctime)s: %(message)s - %(funcName)s:%(lineno)d "  # logging format
        logging.basicConfig(filename=logfile, level=loglevel, format=logfmt, datefmt=dtfmt)
        return logging.getLogger()

logger = set_logger("app.log")


def reveal_Hosts():
    iptxt = entry.get()
    print("This is the data", iptxt)
    check_hosts = (f"sudo nmap -sn {iptxt}/24")

    newcmd =["sudo nmap -sn ",iptxt]


    output = subprocess.check_output(check_hosts,shell=True)
    # output = subprocess.check_output("ping {} -c 2".format(entry.get()), shell=True)   192.168.100.0

    # print('>', output)
    # put result in label
    result['text'] = output.decode('utf-8')





my_gui = tk.Tk()
entry = tk.StringVar()

my_gui.geometry('500x500')
my_gui.title("Get output inside GUI") 
my_gui.eval('tk::PlaceWindow . center')
tk.Label(my_gui, text="Enter the router's IP address").pack() 
tk.Entry(my_gui, textvariable=entry).pack()
tk.Button(my_gui,text="Scan Hosts", command=reveal_Hosts).pack() 

# label for ping result
result = tk.Label(my_gui)
result.pack()

my_gui.mainloop()