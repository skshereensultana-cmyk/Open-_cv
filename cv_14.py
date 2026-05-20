import cv2
video = cv2.VideoCapture(r"C:\Users\shree\Videos\Captures\nature video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("Output.mp4", fourcc, 25.0, (1928,1080))
while video.isOpened():
    ret, frame = video.read()
    if ret:
        output.write(frame)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(10) & 0xFF == ord('s'):
            break
    else:
        break

video.release()
output.release()
cv2.destroyAllWindows()