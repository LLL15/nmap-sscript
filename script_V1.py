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


familiar = input("Are you familiar with Nmap? [Yes/No]: ").lower()


# Tests validation of user's input (yes or no)
def test_input(usrinput):
    while usrinput != 'yes' and usrinput != 'no':
        ask_again = input("Please enter Yes/No: ").lower()
        if ask_again == 'yes' or ask_again == 'no':
            usrinput = ask_again


def test_input2(secondinput):
    while True:
        if secondinput == 'yes':
            start_scan = input("Perform a scan? [Yes/No]: ").lower()
            if start_scan != 'yes' and start_scan != 'no':
                test_input(start_scan)

            else:
                if start_scan == 'yes':
                    # perform_scan(start_scan)
                    print("Performing a scan...")
                    print(scan(input("Enter IP address or Range: "), input("Enter arguments (enter for none):")))
                    break  # Remove this when adding while loop which will ask user to keep scanning
                elif start_scan == 'no':
                    print("Exiting the script... \nGoodbye!")
                    raise SystemExit

        elif secondinput == 'no':
            view_help = input("Do you want to view help? [Yes/No]: ").lower()
            if view_help == 'yes':
                command2 = "nmap --help"
                process2 = os.popen(command2)
                print(str(process2.read()))
                break

            elif view_help == 'no':
                print("Exiting the script... \nGoodbye!")
                raise SystemExit

            else:
                test_input(view_help)

        else:
            test_input(secondinput)


test_input2(familiar)
