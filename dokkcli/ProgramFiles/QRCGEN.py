# Made by Senpai_Desi#4108
# https://www.desidevit.com
import qrcode
from PIL import Image

# Function to generate a qr code based on the message defined later on.
def make_qr():
    # Ask the user to input what they want the qr code to contain
    message = input("What do you want the qr code to contain?\n")
    filename = input("What do you want the qr to be named?\n")
    path_to_qr = input("Where do you want the qr to be saved? (Example: C:)\n")
    new_qr = qrcode.make(message)
    try:
        new_qr.save(f'{path_to_qr}\{filename}.jpg')
    except FileNotFoundError:
        return print("This is not a valid path!")
    print(f"Done! Saved qr to {path_to_qr}\{filename}.jpg!")
