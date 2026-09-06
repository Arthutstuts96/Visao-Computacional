import cv2
import time

from separar_cor import separar_canais_rgb

cap = cv2.VideoCapture(0)
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    curr_time = time.time()
    fps = 1.0 / (curr_time - prev_time) if curr_time != prev_time else 0.0
    prev_time = curr_time

    cv2.putText(frame, f'FPS: {fps:.1f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Câmera Aberta", frame)

    separar_canais_rgb(frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
