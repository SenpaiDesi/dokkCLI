# Setup function 
import os
import colorama
from colorama import Fore
import cli
import time
from ProgramFiles import tracker, passwordcracker, about, zipcracker
def title():
    os.system('TITLE Loading...')
    os.system("cls")
    os.system("yes | pip install colorama --quiet --exists-action ignore")
    os.system("cls")
    os.system("TITLE dokkCLI")


def startup():
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
    print(Fore.RESET + "\n")
    print("Welcome to dokkcli, if this is your first time using this software. Please use module 1 Setup. \n")


def menu_one():
    os.system("cls")
    os.system("TITLE Installing dependencies...")
    os.system("pip install requests -q --exists-action i")
    os.system("pip install pygeoip -q --exists-action i")
    os.system("pip install zipfile -1 --exists-action i")
    print(Fore.GREEN + "[INFO] All dependencies installed and tool is ready to use!")
    time.sleep(3)
    print(Fore.RESET + "\n\n")
    cli.main()

def menu_two():
    os.system('cls')
    os.system('TITLE  [DOKKCLI]    Network Attacks:')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n\n")
    menu_select = input(Fore.GREEN + "[1]    ipinfo.\n[2]    Soon to come\n[3]    Soon to come\n[4]    Soon to come\n[5]    Soon to come\n[6]    Soon to come.\n\n")
    if str(menu_select) == "1":
        tracker.print_record()
        os.system('pause')
        cli.main()
    else:
        print("Soon to come")
        os.system('pause')
        cli.main()

# password related menu
def menu_three():
    os.system('cls')
    os.system('TITLE [DOKKCLI]    Password attacks')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n\n")
    menu_select = input(Fore.GREEN + "[1]    Users.\n[2]    Zip files\n[3]    Soon to come\n[4]    Soon to come\n[5]    Soon to come\n[6]    Soon to come.\n\n")
    # User password cracker software which compares hashes.
    if str(menu_select) == "1":
        passwordcracker.main()
        os.system('pause')
        cli.main()
        # attempts to crack a password protected zip file.
    elif str(menu_select) == "2":
        os.system('cls')
        os.system('title [DOKKCLI]    ZIP CRACKER')
        zipcracker.zipfilecrack()
        os.system('pause')
        cli.main()


    else:
        print("Soon to come!")
        os.system('pause')
        cli.main()

def menu_five():
    os.system('cls')
    os.system('title [DOKKCLI]    Information')
    about.info_print()
    os.system('pause')
    cli.main()


def menu_zero():
    os.system('cls')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
    print(Fore.RESET + "Thanks for using DOKK CLI!      Made by Senpai_Desi#4108\n")
    os.system('exit')