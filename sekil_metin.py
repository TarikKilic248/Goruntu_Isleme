# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:11:16 2024

@author: batma
"""

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8) #zeros = siyah goruntu
print(img.shape)

cv2.imshow("Siyah", img)
cv2.waitKey(0)

#cizgi (resim, baslangic, bitis, renk, kalinlik)
cv2.line(img, (50,50), (400,400), (0,255,0), 3)
cv2.imshow("Cizgi", img)
cv2.waitKey(0)

#dikdortgen (resim, baslangic, bitis, renk)
cv2.rectangle(img, (50,50), (400,400), (255,255,0))
cv2.imshow("Dikdortgen", img)
cv2.waitKey(0)

cv2.rectangle(img, (150,150), (300,300), (255,255,0), cv2.FILLED)
cv2.imshow("Dikdortgen", img)
cv2.waitKey(0)

#circle (resim, merkez, yaricap, renk)
cv2.circle(img, (350,150), 45, (255, 0,255))
cv2.imshow("Circle", img)
cv2.waitKey(0)

cv2.circle(img, (350,450), 45, (255, 0,255), cv2.FILLED)
cv2.imshow("Circle", img)
cv2.waitKey(0)

#metin (resim, baslangic, font, kalinlik, renk)
cv2.putText(img, "Resim", (150,400), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)
cv2.waitKey(0)


cv2.destroyAllWindows()