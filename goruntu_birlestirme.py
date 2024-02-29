# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:26:26 2024

@author: batma
"""

import cv2
import numpy as np

img = cv2.imread("messi.jpg", 1)
cv2.imshow("messi", img)
cv2.waitKey(0)

#yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)
cv2.waitKey(0)

#dikey
ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)
cv2.waitKey(0)






cv2.destroyAllWindows()