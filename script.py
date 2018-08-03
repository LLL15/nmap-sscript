#! /usr/bin/python3

import os
import re

ipaddr = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')


def scan(ip, args=''):
    while ipaddr.search(ip) is None:
        ip = input('Please enter correct IP|IP Range: ')
        if ipaddr.search(ip) is not None:
            break

    command = "nmap " + args + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results


view_help_nmap = input("Do you want to view Nmap help page before scanning [yes|no]: ").lower()


def view_help(userinp):
    if userinp == 'yes':
        command = 'nmap --help'
        process = os.popen(command)
        print(str(process.read()))
        quit_or_continue = input("Start scan now [yes|no]: ").lower()
        if quit_or_continue == 'yes':
            print('\n')
            start_scan()
        else:
            print("Exiting the script . . .")
            raise SystemExit
    elif userinp == 'no':
        print('\n')
        start_scan()


def start_scan():
    while 1:
        print("Performing a scan...")
        print(scan(input("Enter IP address or Range: "), input("Enter arguments (enter for none):")))
        scan_again = input("Do you want to keep scanning [yes|no]: ").lower()
        if scan_again == 'yes':
            continue
        elif scan_again == 'no':
            break
    print("Exiting the script . . .")
    raise SystemExit


view_help(view_help_nmap)
