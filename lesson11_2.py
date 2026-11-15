import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("132849-754950619_small.mp4")
width = 640
height = 480
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)
counted_ids = set()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (width, height))
    results = model.track(frame, persist=True, classes = [2], verbose = False)
    cars_in_frame = 0
    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy().astype(int)
        confs = results[0].boxes.conf.cpu().numpy()
        for box, track_id, conf in zip(boxes, ids, confs):
            x1, y1, x2, y2 = map(int, box)
            cars_in_frame += 1
            if track_id not in counted_ids:
                counted_ids.add(track_id)
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 0, 255),
                2
            )
            cv2.putText(
                frame,
                f"ID:(track_id)",
                (x1, y1 - 30),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                0.6,
                (255, 255, 0),
                2
            )
            cv2.putText(
                frame,
                f"{conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )
    cv2.putText(
            frame,
            f"Cars in Frame : {cars_in_frame}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )
    cv2.putText(
            frame,
            f"Total Cars : {len(counted_ids)}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )
    out.write(frame)
    cv2.imshow("YOLOv8 Car Tracking", frame)
    if cv2.waitKey(1) == 27:
            break
cap.release()
out.release()
cv2.destroyAllWindows()