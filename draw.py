import cv2
import sys

sys.path.append('/Users/calebvandermaas/cd/lib/python3.9/site-packages')
import base64


def encode_image():
    img = cv2.imread('Documents/monaLisa.bin')
    image = cv2.imencode('.bin', img)[1]
    print(image)
    print(base64.b64encode(image).decode())
    return base64.b64encode(image).decode()
