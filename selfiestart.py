import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('harcascade_frontlface_default.xml')
smile_cascade = cv2.CascadeClassifier('harcascade_smile.xml')
while True:
    _, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, 1.3, 5)
for x, y, w, h, in face:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    face_roi = frame[y:y+h, x:x+w]
    gray_roi = gray[y:y+h, x:x+w]
    smile = smile_cascade.detectMultiScale(gray+roi, 1.3, 25)
    for x1, y1, w1, h1 in smile:
        cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2) 
        cv2.imwrite('selfie.png', frame)
    cv2.imshow('cam star', frame)
    if cv2.waitKey(10) == ord('q'):
        break