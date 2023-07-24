import cv2
from gtts import gTTS
from IPython.display import Audio


url = 'http://192.*.*.*:****/video'

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Unable to connect to camera")
else:
    qr_detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        data, points, _ = qr_detector.detectAndDecode(frame)
        if data:
            print(f'QR code data: {data}')
            tts = gTTS(data)
            tts.save('qr.mp3')
            Audio('qr.mp3')
            
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break
            
cap.release()
cv2.destroyAllWindows()


