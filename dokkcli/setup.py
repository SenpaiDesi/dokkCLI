# Setup function 
import os
import colorama
from colorama import Fore
import cli
import time
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
    print(Fore.GREEN + "[INFO] All dependencies installed and tool is ready to use!")
    time.sleep(3)
    print(Fore.RESET + "\n\n")
    os.system('pause')
    cli.main()