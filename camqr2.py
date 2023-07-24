import cv2
import pyzbar.pyzbar as pyzbar
from playsound import playsound


img = cv2.imread('channel.png')
url = 'http://192.*.*.*:****/video'
cap = cv2.VideoCapture(url)

while True:
    _, frame = cap.read()
    cv2.imshow("Frame", frame)

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:

        if len(obj) >= 1:
            import webbrowser
            webbrowser.open(obj.data.decode('utf-8'))
        

    key = cv2.waitKey(1)
    if key == 27:
        break