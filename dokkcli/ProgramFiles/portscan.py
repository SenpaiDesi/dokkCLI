
from concurrent.futures import ThreadPoolExecutor
import subprocess
import sys
from datetime import date, datetime
from socket import *
from threading import Thread
from colorama import Fore


def scan():
    #Ask for inpute
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = gethostbyname(remoteServer)

    # time and information
    current_time = datetime.now()
    print(Fore.RESET + "\n")

    try:
        # Defining ports using range()
        # Error handeling included

        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            print(f"Scanning {port} on {remoteServerIP}\n")
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(1)
         
            # returns an error indicator
            result = s.connect_ex((remoteServerIP,port))
            if result ==0:
                print(Fore.GREEN + "Port {} is open".format(port))
                print(Fore.RESET())
            s.close()
         
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except error:
        print("\ Server not responding !!!!")
        sys.exit()

    #check time again
    current_time_two = datetime.now()

    # Calculate elapsed time
    elapsed_time = current_time_two - current_time

    # Print result to the screen
    print("-" * 100)
    print("FINISHED IN :", elapsed_time)
    print("-" * 100)

if __name__ == "__main__":
    scan()