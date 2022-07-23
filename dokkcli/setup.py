# Setup function 
import os
from colorama import Fore
from colorama.ansi import clear_screen
import cli
import time
import subprocess
from ProgramFiles import information
from ProgramFiles import tracker, passwordcracker, zipcracker, incognito, calendar, QRCGEN, QRCReader, remoteshellserv, remoteshellclient, portscan

def title():
    os.system('TITLE Loading...')
    os.system("cls")
    os.system("yes | pip install colorama --quiet --exists-action i")
    os.system("cls")
    os.system("TITLE dokkCLI")


def startup():
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
    print(Fore.RESET + "\n")
    print("Welcome to dokkcli, if this is your first time using this software. Please use module 1 Setup. \n")


# hacking menus



def hack_menu_one():
    os.system('cls')
    os.system('TITLE  [DOKKCLI]    Network Attacks:')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n\n")
    menu_select = input(Fore.GREEN + "[1]    ipinfo.\n[2]    Remote shell\n[3]    Port Scanner\n[4]    Soon to come\n[5]    Soon to come\n[6]    Soon to come.\n\n")
    if str(menu_select) == "1":
        tracker.print_record()
        os.system('pause')
        cli.main()
    if str(menu_select) == "2":
        os.system('cls')
        os.system('TITLE  [DOKKCLI]    Remote shell Attacks:')
        print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n\n")
        remoteshell_men = input(Fore.GREEN + "[1]    Remote shell Server\n[2]    Remote Shell Client.\n")
        if str(remoteshell_men) == "1":
            os.system('cls')
            remoteshellserv.Listen()
            os.system('pause')
            cli.main()
        elif str(remoteshell_men) == "2":
            remoteshellserverip = input("Enter remote shell server ip: ")
            remoteshellclient.clientcon(str(remoteshellserverip))
            cli.main()
    if str(menu_select) == "3":
        os.system('cls')
        portscan.scan()
        os.system('pause')
        cli.main()
    else:
        print("Soon to come")
        os.system('pause')
        cli.main()

# password related menu
def hack_menu_two():
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
    
def hack_menu_three():
    os.system('cls')
    os.system('title [DOKKCLI]    Anon Page downloader.')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n\n")
    incognito.visit()
    os.system('pause')
    cli.main()

def hack_menu_zero():
    os.system('cls')
    print("Sorry this does not exist yet. Soon to come!")
    cli.main()


# normal menus
def menu_zero():
    os.system('cls')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
    print(Fore.GREEN + "Thanks for using DOKK CLI!      Made by Senpai_Desi#4108\n")
    os.system('TIMEOUT 5')
    os.system('exit')






def menu_five():
    os.system('cls')
    os.system('title [DOKKCLI]    Information')
    information.information_printer()
    os.system('pause')
    cli.main()

def menu_undefined():
    os.system('cls')
    print(Fore.RED + "This does not exist yet. Will be developed later on.")
    os.system('pause')
    os.system('cls')
    cli.main()

def menu_unselected():
    os.system('cls')
    print(Fore.RED + "You did not select a option, returning to main menu!")
    os.system('TIMEOUT 3')
    os.system('cls')
    cli.main()



# post install and update menu

def update_menu():
    os.system('TITLE [DOKKCLI]    UPDATING....')
    os.system('cls')
    os.system('pip install --upgrade pip --quiet')
    os.system('pip install --upgrade mechanize --quiet')
    os.system('pip install --upgrade pygeoip --quiet')
    os.system('TITLE [DOKKCLI]    DONE!')
    os.system('TIMEOUT 5')
    cli.main()
    



# global tools menu

def calendar_tool():
    os.system('cls')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
    print(Fore.RESET + "\n")
    os.system('TITLE DOKKCLI    CALENDAR')
    calendar.StartCalendar()
    cli.main()

def qrmaker_tool():
    os.system('cls')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
    print(Fore.RESET + "\n")
    os.system('TITLE DOKKCLI    QR-CODE maker.')
    QRCGEN.make_qr()
    os.system('pause')
    cli.main()
    

def qrreader_tool():
    os.system('cls')
    print(Fore.RED + "██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗██╗     ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝    ██╔════╝██║     ██║\n██║  ██║██║   ██║█████╔╝ █████╔╝     ██║     ██║     ██║\n██║  ██║██║   ██║██╔═██╗ ██╔═██╗     ██║     ██║     ██║\n██████╔╝╚██████╔╝██║  ██╗██║  ██╗    ╚██████╗███████╗██║\n")
    print(Fore.RESET + "\n")
    os.system('TITLE DOKKCLI    QR-CODE reader.')
    QRCReader.readqr()
    os.system('pause')
    cli.main()