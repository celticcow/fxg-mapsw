#!/usr/bin/python3

import sys
import string
import ipaddress
import socket

"""
"""

def main():
    print("start of main")

    debug = 1

    site_num = input("enter site number : ")

    for x in (list(string.ascii_lowercase)):
        #print(x)

        for y in range (1, 10):
            #print(y)

            name = "fxg" + site_num + "sw" + x + str(y) + ".ground.fedex.com"
            
            try:
                ip_addr = socket.gethostbyname(name)
                print(name)
                print(ip_addr)
            except:
                pass

if __name__ == "__main__":
    main()