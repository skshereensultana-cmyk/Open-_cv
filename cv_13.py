import cv2

video = cv2.VideoCapture(r"C:\Users\shree\Videos\Captures\nature video.mp4")

while video.isOpened():
    ret, frame = video.read()

    frame = cv2.resize(frame, (880,728))

    cv2.imshow("Output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()