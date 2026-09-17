import cv2

cap = cv2.VideoCapture("camera/videos/dog.mp4")

while True:
    _, frame = cap.read()
    if not _:
        break

    cv2.imshow('Câmera Aberta', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()