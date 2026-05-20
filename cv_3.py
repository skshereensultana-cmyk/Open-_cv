import cv2

img = cv2.imread(r"C:\Users\shree\OneDrive\Pictures\Screenshots 1\Screenshot 2026-05-20 152822.png")

width = 600
height = 850
dim = (width, height)

resized = cv2.resize(img, dim)

print('Size in bytes:', img.size)

cv2.imshow('Original', resized)

#flip = cv2.flip(resized, 1)
#cv2.imshow('Horizontal', flip)

#flip_1 = cv2.flip(resized, 0)
#cv2.imshow('Vertical', flip_1)

flip_2 = cv2.flip(resized, -1)
cv2.imshow('Horizontal & Vertical', flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()