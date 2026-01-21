import cv2
import numpy as np
from transformers import pipeline

object_detector = pipeline("object-detection")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    results = object_detector(frame)

    for obj in results:
        x, y, w, h = int(obj['box']['xmin']), int(obj['box']['ymin']), int(obj['box']['xmax']), int(obj['box']['ymax'])
        label = obj['label']
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("AI Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()