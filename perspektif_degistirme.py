# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:31:52 2024

@author: batma
"""

import cv2
import numpy as np

img = cv2.imread("messi.jpg", 1)
print(img.shape)
cv2.imshow("messi", img)
cv2.waitKey(0)

width = 474
height = 340

#cevirmek istedigim resmin koseleri
pts1 = np.float32([[0,0], [0,474], [340,0], [340,473]])

#duzlestirmek istedigim resmin koseleri
pts2 = np.float32([[100,0], [0,374], [340,374], [240,474]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("donen messi", imgOutput)
cv2.waitKey(0)



cv2.destroyAllWindows()