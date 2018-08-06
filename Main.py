#! /usr/bin/python3

import os
import re

# This ipaddr holds regex that will be used for matching correctly formed IP addressess and optionally CIDR notation.
ipaddr = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(/\d{1,2})?$')

try:
    def scan(ip, args=''):  # This is where it actually starts a nmap scan...
        while ipaddr.search(ip) is None:
            ip = input('Please enter correct IP: ')
            if ipaddr.search(ip) is not None:
                break

        command = "nmap " + args + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results


    view_help_nmap = input("Do you want to view Nmap help page before scanning [Y|N]: ").lower()


    def view_help(userinp):  # This function allows user to view nmap help page

        if userinp == 'yes' or userinp == 'y' or userinp == '':
            command = 'nmap --help'
            process = os.popen(command)
            print(str(process.read()))
            quit_or_continue = input("Start scan now [Y|N]: ").lower()

            if quit_or_continue == 'yes' or quit_or_continue == 'y' or quit_or_continue == '':
                start_scan()

            else:
                print("Exiting the script . . .")
                raise SystemExit

        elif userinp == 'no' or userinp == 'n':
            start_scan()

   
    def start_scan():  # This is where it calls scan() function to perform a scan over and over until user stops it.
        while 1:
            print(' ')
            print("Performing a scan...")
            print(scan(input("Enter IP address: "), input("Enter arguments (enter for none):")))

            scan_again = input("Do you want to keep scanning [Y|N]: ").lower()

            if scan_again == 'yes' or scan_again == 'y' or scan_again == '':
                continue

            elif scan_again == 'no' or scan_again == 'n':
                break

        print("Exiting the script . . .")
        raise SystemExit


    view_help(view_help_nmap)
except KeyboardInterrupt:
    print("\n\nProgram is terminated")
    print("\nExiting the script...")
except Exception:  # Program is stopped if error occurs or user terminates the program
    print("\n\n(!)Unknown error occurred(!)")
    print("\nExiting the script...")
