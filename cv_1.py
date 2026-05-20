import cv2

img = cv2.imread(r"C:\Users\shree\OneDrive\Pictures\Screenshots 1\Screenshot 2026-05-16 101406.png",)

if img is None:
    print("Image not found. Check the path.")
else:
    cv2.imshow("Window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    