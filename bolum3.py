import cv2

#resmi ice aktarma  0 = gri
img = cv2.imread("messi.jpg", 0)

#resmi goruntuleme
cv2.imshow("First Image", img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()
    
