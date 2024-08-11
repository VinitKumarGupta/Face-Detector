import cv2

vid = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

while True:
    success, frame = vid.read()

    if success:
        gray_scale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray_scale_frame, 1.3, 3)

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (225, 0, 0), 3)
        cv2.imshow("Output Stream", frame)

        if cv2.waitKey(1) & 0xFF == ord("1"):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()