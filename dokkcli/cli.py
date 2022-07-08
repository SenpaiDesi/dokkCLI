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
    menu_select = input(Fore.GREEN + "[1]    Setup.\n[2]    tools and scripts\n[3]    To be Made\n[4]    To be made\n[5]    Information.\n[0]    Exit\n\n")

    # Showcase submenu
    if str(menu_select) == "1":
         setup.hack_menu_one()
    elif str(menu_select) == "2":
        os.system('cls')
        setup.startup()
        hack_menu_select = input(Fore.GREEN + "[1]    Setup.\n[2]    Network attacks\n[3]    Password cracking\n[4]    Page downloader\n[5]    Soon to come.\n[0]    Exit\n\n")
        if str(hack_menu_select) == "1":
            setup.hack_menu_one()
        elif str(hack_menu_select) == "2":
            setup.hack_menu_two()
        elif str(hack_menu_select) == "3":
            setup.hack_menu_three()
        elif str(hack_menu_select) == "4":
            setup.hack_menu_four()
        elif str(hack_menu_select) == "5":
            setup.menu_undefined()
        elif str(hack_menu_select) == "0":
            setup.hack_menu_zero()


    elif str(menu_select) == "3":
        setup.menu_undefined
    elif str(menu_select) == "5":
        setup.menu_undefined
    elif str(menu_select) == "0":
        setup.menu_undefined()


if __name__ == "__main__":
    main()