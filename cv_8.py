import cv2
import numpy as np
img = cv2.imread(r"C:\Users\shree\OneDrive\Pictures\Screenshots 1\Screenshot 2026-05-20 152822.png", 0)
threshold_value = 180
_, binary_threshold = cv2.threshold(
    img,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)
cv2.imshow('Original', img)
cv2.imshow('Binary Threshold', binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()