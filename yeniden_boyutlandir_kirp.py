# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:55:31 2024

@author: batma
"""

import cv2

img = cv2.imread("doctor.png", 1)
print("Resim boyutu", img.shape)
cv2.imshow("Orijinal", img)
cv2.waitKey(0)


img_resized = cv2.resize(img, (800,800))
cv2.imshow("Resized Image", img_resized)
cv2.waitKey(0)

#resim kirpma
img_cropped = img[0:200, 0:700]
cv2.imshow("kirpilmis", img_cropped)
cv2.waitKey(0)

cv2.destroyAllWindows() 