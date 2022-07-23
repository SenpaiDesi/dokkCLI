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
    menu_select = input(Fore.GREEN + "[1]    Update.\n[2]    tools and scripts\n[3]    Global Tools\n[4]    To be made\n[5]    Information.\n[0]    Exit\n\n")

    # Showcase submenu
    if str(menu_select) == "1":
         setup.update_menu()
    elif str(menu_select) == "2":
        os.system('cls')
        setup.startup()
        hack_menu_select = input(Fore.GREEN + "[1]    Network attacks.\n[2]    Password cracking\n[3]    Page downloader\n[4]    Soon to come.\n[5]    Soon to come.\n[0]    Exit\n\n")
        if str(hack_menu_select) == "1":
            setup.hack_menu_one()
        elif str(hack_menu_select) == "2":
            setup.hack_menu_two()
        elif str(hack_menu_select) == "3":
            setup.hack_menu_three()
        elif str(hack_menu_select) == "4":
            setup.menu_undefined()
        elif str(hack_menu_select) == "5":
            setup.menu_undefined()
        elif str(hack_menu_select) == "0":
            setup.hack_menu_zero()


    elif str(menu_select) == "3":
        os.system('cls')
        print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
        print(Fore.RESET + "\n")
        global_tools_menu = input(Fore.GREEN + "[1] Calendar\n[2] QR code maker\n[3] QR code reader\nEnter your choice: ")
        if str(global_tools_menu) == "1":
            setup.calendar_tool()
        elif str(global_tools_menu) == "2":
            setup.qrmaker_tool()
        elif str(global_tools_menu) == "3":
            setup.qrreader_tool()
        else:
            setup.menu_undefined()
    elif str(menu_select) == "5":
        setup.menu_five()
    elif str(menu_select) == "0":
        setup.menu_zero()
    else:
        setup.menu_unselected()

if __name__ == "__main__":
    main()