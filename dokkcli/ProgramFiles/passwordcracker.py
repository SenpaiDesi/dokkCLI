from colorama import Fore
import cli
import os
try:
    import crypt
except ImportError or ModuleNotFoundError:
    print(" ERROR User cracking is not supported on Windows platforms so can not be used. Please use linux / unix instead!")
    os.system('pause')

def cracker(cryptPass):
    global passfile
    salt = cryptPass[0:2]
    tries = 0

    print("-" * 100)
    print("Please input the file location with extension for the list...")
    print("-" * 100)
    dictfile = input("Provide full path + extension. Example: Path/To/File.txt")

    dictfile = open(dictfile, 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word.salt)
        tries + 1
        if cryptWord == cryptPass:
            print(f"Password Found at try {tries}! Password {word}")
        print("No password was found!")    
        return
    
def main():
    passFile_request = input("Please provide the path to the password file: ")
    try:
        passFile = open(passFile_request)
    except Exception as e:
        os.system('cls')
        print(Fore.BLUE + f"Error, {e}")
        os.system('pause')
        cli.main()
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print(f"Cracking password for {user}")
            cracker(cryptPass)
