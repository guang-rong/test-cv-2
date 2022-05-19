import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break


gray = cv2.cvtColor(cap, cv2.COLOR_BGRA2GRAY)
faceCascade = cv2.CascadeClassifier('face_defect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 1)

for (x,y,w,h) in faceRect:
    cv2.rectangle(cap, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow('cap', cap)