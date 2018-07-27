"""
TO-DO:
1. Add more input validation
2. Add an option for user to view man page of nmap
"""

import os
import re

ipaddr = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')


def scan(ip, args=''):
    while ipaddr.search(ip) is None:
        ip = input('Please enter correct IP/IP Range: ')
        if ipaddr.search(ip) is not None:
            break

    command = "nmap " + args + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results


familiar = input("Are you familiar with Nmap [Yes/No]: ").lower()

while familiar != 'yes' and familiar != 'no':
    again = input("Please enter Yes/No: ").lower()
    if again == 'yes' or again == 'no':
        familiar = again
        break

while familiar == 'yes' or familiar == 'no':
    if familiar == "yes":
        print(scan(input("Enter IP address or Range: "), input("Enter arguments (enter for none):")))
        break

    elif familiar == "no":
        view_help = input('Do you want to view help')
        command2 = "nmap --help"
        process2 = os.popen(command2)
        print(str(process2.read()))
        break

