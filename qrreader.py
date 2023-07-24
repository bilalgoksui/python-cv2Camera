import cv2


url = 'http://192.*.*.*:****/video'

cap = cv2.VideoCapture(url)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

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
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
