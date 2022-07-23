import cv2



def readqr():
    file = input("Please provide the filepath with file and extension to the qr code.\n")
    detect = cv2.QRCodeDetector()
    val, _, _ = detect.detectAndDecode(cv2.imread(file))
    print(f"Decoded qr code value is:\n {val}")