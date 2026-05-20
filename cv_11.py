import cv2

img = cv2.imread(r"C:\Users\shree\OneDrive\Pictures\Screenshots 1\Screenshot 2026-05-16 101406.png")
resize = cv2.resize(img, (628,520))

d = 7
sigmacolor = 180
sigmaspace = 100

b = cv2.bilateralFilter(resize, d, sigmacolor, sigmaspace)

cv2.imshow("Input", resize)
cv2.imshow("Output", b)

cv2.waitKey(0)
cv2.destroyAllWindows()