import cv2

img = cv2.imread(r"C:\Users\shree\OneDrive\Pictures\Screenshots 1\Screenshot 2026-05-20 152822.png  ")
resize = cv2.resize(img, (528,520))

kernel = 3

blur = cv2.medianBlur(resize, kernel)

cv2.imshow("Input", resize)
cv2.imshow("Output", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()