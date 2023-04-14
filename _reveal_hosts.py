import subprocess


def reveal_Hosts(router_Ip):

    print("This is the data", router_Ip)
    check_hosts = (f"sudo nmap -sn {router_Ip}/24")

    newcmd =["sudo nmap -sn ",router_Ip]


    output = subprocess.check_output(check_hosts,shell=True)
    # output = subprocess.check_output("ping {} -c 2".format(entry.get()), shell=True)   192.168.100.0

    print('>', output)
    # put result in label
    result['text'] = output.decode('utf-8')   #change the result to anything you wanted to place the result