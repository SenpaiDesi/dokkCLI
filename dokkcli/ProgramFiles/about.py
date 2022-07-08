from colorama.ansi import Fore


Author = "Senpai_Desi"
Contributors = ["Root Beer"]
Version = "v0.4"
About = "DOKKCLI (Also known as Dokkaebi CLI) Is a multi-tool Command Line Interface made with python\nWhich contains a large set of python made offensive tools.\nMade Originally as a honor towards UbiSoft and Their game Rainbow Six Siege, we decided to bring DOKK alive.\nSo here it is. A WIP tool that actually does its job where it needs to.\nWe hope to one day implement the real dokk os hack. But no promises..."

def info_print():
    print(Fore.GREEN + f"Author:{Author}\n")
    print(f"Contributors: {Contributors[0]}\n")
    print(f"Version: {Version}\n")
    print(f"About: {About}\n")