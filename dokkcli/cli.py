import os
import setup
from colorama import Fore

# Setting main title

def main():
    #Setup the window
    setup.title()
    setup.startup()

    # Global variable We use later on for the code execution
    global menu_select
    print("Select one of the Categories below.\n")

    # Get user input for categoy and show the corresponding sub menu.
    menu_select = input(Fore.GREEN + "[1]    Setup.\n[2]    Network Attacks\n[3]    IP Information\n[4]    Password Attaks\n[5]    Anonymous page downloader\n[6]    Information.\n\n")

    # Showcase submenu
    if str(menu_select) == "1":
         setup.menu_one()

if __name__ == "__main__":
    main()