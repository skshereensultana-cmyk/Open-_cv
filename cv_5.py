import cv2
import numpy as np
img = cv2.imread(r"C:\Users\shree\OneDrive\Pictures\Screenshots 1\Screenshot 2026-05-20 152822.png", cv2.IMREAD_COLOR)

img = np.zeros([600, 800, 3])
img = np.zeros(shape=[600, 800, 3], dtype='uint8')

img.fill(255)
cv2.line(img, (80, 80), (150, 150), (255, 0, 0), 2)
cv2.rectangle(img, (200, 150), (250, 300), (0, 255, 0), 3)
cv2.circle(img, (500, 75), 70, (255, 0, 255), 3)
pts_polygon = np.array([[100, 50], [100, 100], [500, 50], [580, 300]], np.int32)
cv2.polylines(img, [pts_polygon], True, (0, 255, 255), 3)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'HELLO', (100, 500), font, 3, (200, 255, 255), 1, cv2.LINE_AA)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()