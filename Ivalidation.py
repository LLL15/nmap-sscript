#! /usr/bin/python3

import os
import re


# This ipaddr holds regex that will be used for matching correctly formed IP addressess and optionally CIDR notation.
ipaddr = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(/\d{1,2})?$')
# These sets hold the values of accepted answers when asked for input
yes_answer = {'yes', 'y', ''}
no_answer = {'no', 'n'}


try:
    def validation(test_input):
        while 1:
            new_input = input("Please enter correct input [Y|N]: ")
            if new_input in yes_answer or new_input in no_answer:
                return test_input.replace(test_input, new_input)
            else:
                continue


    def scan(ip, args=''):  # This is where it actually starts a nmap scan...
        while ipaddr.search(ip) is None:
            ip = input('Please enter correct IP: ')
            if ipaddr.search(ip) is not None:
                break

        command = "nmap " + args + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results


    def view_help(userinp):  # This function allows user to view nmap help page
        while 1:
            if userinp in yes_answer or userinp in no_answer:
                if userinp in yes_answer:
                    command = 'nmap --help'
                    process = os.popen(command)
                    print(str(process.read()))
                    quit_or_continue = input("Start scan now [Y|N]: ").lower()
                    while 1:
                        if quit_or_continue in yes_answer:
                            start_scan()

                        elif quit_or_continue in no_answer:
                            print("Exiting the script . . .")
                            raise SystemExit
                        else:
                            quit_or_continue = validation(quit_or_continue)
                            continue

                if userinp in no_answer:
                    start_scan()

            elif userinp not in yes_answer or userinp not in no_answer:
                userinp = validation(userinp)
                continue

    def start_scan():  # This is where it calls scan() function to perform a scan over and over until user stops it.
        while 1:
            print(' ')
            print("Performing a scan...")
            print(scan(input("Enter IP address: "), input("Enter arguments (enter for none):")))

            scan_again = input("Do you want to keep scanning [Y|N]: ").lower()
            if scan_again in yes_answer or scan_again in no_answer:
                if scan_again in yes_answer:
                    continue

                elif scan_again in no_answer:
                    break

            elif scan_again not in yes_answer or scan_again not in no_answer:
                scan_again = validation(scan_again)
                if scan_again in yes_answer:
                    continue

                elif scan_again in no_answer:
                    break

        print("Exiting the script . . .")
        raise SystemExit

    view_help_nmap = input("Do you want to view Nmap help page before scanning [Y|N]: ").lower()

    view_help(view_help_nmap)

except KeyboardInterrupt:  # Program is stopped if user terminates the program
    print("\n\nProgram is terminated")
    print("\nExiting the script...")

except Exception:  # Program is stopped if error occurs
    print("\n\n(!)Unknown error occurred(!)")
    print("\nExiting the script...")
