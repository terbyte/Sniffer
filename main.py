#EITHER I CAN USE TKINTER/ QT5 /  KIVY
# import nmap
import os
import tkinter as tk
import subprocess
import logging
import time


def set_logger(logfile):
        logfile =  logfile  # prepend path "logs/"
        loglevel = logging.INFO  # adjust as desired
        dtfmt = '%m/%d/%Y %I:%M:%S %p'
        logfmt = "%(levelname)s: %(asctime)s: %(message)s - %(funcName)s:%(lineno)d "  # logging format
        logging.basicConfig(filename=logfile, level=loglevel, format=logfmt, datefmt=dtfmt)
        return logging.getLogger()

logger = set_logger("app.log")


fileName = 'History.txt'

def file_Writer(lines):
    with open(fileName, 'w') as f:
        f.write('\n')
        f.writelines(lines)


def file_Reader():
    file = open(fileName)  
    # read the content of the file opened
    content = file.readlines()
    
    # read 10th line from the file
    print("tenth line")
    print(content[9])
    
    # print first 3 lines of file
    print("first three lines")
    print(content[0:3])


def file_Reader_Desired():
    file = open(fileName)

    specified_lines = [1, 7, 11]

    # my_list = [1, 5, 4, 6, 8, 11, 3, 12]

    new_list = list(map(lambda x: x * 2 , specified_lines))
    # print(new_list)


    for pos, l_num in enumerate(file):
        if pos in new_list:
            print(l_num)



####################################################3


def reveal_Hosts():
    iptxt = entry.get()
    print("This is the data", iptxt)
    check_hosts = (f"sudo nmap -sn {iptxt}/24")
    percent_spacer = " "

    newcmd =["sudo nmap -sn ",iptxt]


    output = subprocess.check_output(check_hosts,shell=True)
    percentLoader = subprocess.check_output(percent_spacer,shell=True)

    # timer.timeout.connect(TimeSetter)
    # TimeSetter()
    # timer.start(5000)


    # print('>', output)
    # put result in label
    result['text'] = output.decode('utf-8')

    file_Writer(str(result['text']))
    # file_Reader()
    file_Reader_Desired()



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