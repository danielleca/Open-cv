import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

webcam = cv2.VideoCapture(1)

smile_count = 0
REQUIRED_FRAMES = 5

while True:
    _, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=6
    )

    smile_detected = False

    for x, y ,w, h in faces:
       cv2.rectangle(frame, (x, y ), (x + w, y + h), (255, 0, 0), 2)

       face_gray = gray[y + int(h * 0.45) : y + h, x:x + w]
       face_color = frame[y + int(h * 0.45) : y + h, x:x + w]

       smiles = smile_cascade.detectMultiScale(
         face_gray, scaleFactor=1.7, minNeighbors=25, minSize=(25, 15)
       )

       if len(smiles) > 0:
            smile_detected = True

            for sx, sy, sw, sh in smiles:
                cv2.rectangle(
                    face_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2
                )
    if smile_detected:
        smile_count += 1
    else:
        smile_count = max(0, smile_count - 1)

    if smile_count >= REQUIRED_FRAMES:
        cv2.putText(
            frame,
            "SMILE DETECTED!",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3,
        )   
    else:
        cv2.putText(
            frame,
            "No Smile",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )    
    cv2.putText(
        frame,
        "Smile confidence: "+str(smile_count) + "/5",
        (30, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )

    cv2.imshow("Stable Smile Detector", frame)

    key = cv2.waitKey(10)

    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()