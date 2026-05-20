import cv2
import numpy as np

img = cv2.imread(r"C:\Users\shree\OneDrive\Pictures\Screenshots 1\Screenshot 2026-05-20 152822.png")
resize = cv2.resize(img, (520,520))

min_thresh = 100
max_thresh = 200

edges = cv2.Canny(resize, min_thresh, max_thresh)

cv2.imshow("Original", resize)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()