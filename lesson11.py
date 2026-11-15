import cv2
import os

if not os.path.exists("detected_cars"):
    os.makedirs("detected_cars")

car_cascade = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture("132849-754950619_small.mp4")

img_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (800,600))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    cars = car_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (40, 40)
    )

    for (x, y, w, h) in cars:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255),2)

        car_crop = frame[y:y+h, x:x+w]

        img_name = f"detected_cars/car_(img_count).jpg"

        cv2.imwrite(img_name, car_crop)

        img_count += 1

    cv2.putText(frame,
            "Cars detected: "+str(len(cars)),
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
    )
    cv2.imshow("Car Detection", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break
cap.release()

cv2.destroyAllWindows()