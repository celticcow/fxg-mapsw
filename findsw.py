#!/usr/bin/python3

import sys
import string
import ipaddress
import socket
import time

"""
"""
def connect(ip):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a_socket.settimeout(0.5)

    location = (ip, 22)

    result = a_socket.connect_ex(location)

    if(result == 0):
        return True
    else:
        return False
# end connect

def main():
    print("start of main")

    debug = 1

    site_name  = input("enter site name : ")
    site_num   = input("enter site number : ")

    local_grp_name = site_name + "-sw"

    print("group," + local_grp_name + ",FXG-SW")
    for x in (list(string.ascii_lowercase)):
        #print(x)

        for y in range (1, 10):
            #print(y)
            time.sleep(0.5)

            name = "fxg" + site_num + "sw" + x + str(y) + ".ground.fedex.com"
            
            try:
                ip_addr = socket.gethostbyname(name)
                #print(name)
                #print(ip_addr)

                if(connect(ip_addr)):
                    #print("ALIVE", end=" ")
                    #print(name, end=" ")
                    #print(ip_addr, end="\n")

                    print("host," + ip_addr + "," + local_grp_name)

                else:
                    pass
                    #print("NO CONN", end=" ")
                    #print(name, end=" ")
                    #print(ip_addr, end="\n")
            except:
                pass

if __name__ == "__main__":
    main()