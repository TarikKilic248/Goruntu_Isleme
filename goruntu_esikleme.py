# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 11:39:34 2024

@author: batma
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("taken.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#esikleme
_, tresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(tresh_img, cmap="gray")
plt.axis("off")
plt.show()

#adaptif esikleme
adaptif_tresh_img = cv2.adaptiveThreshold(img, maxValue=255,
                                  adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                                  thresholdType=cv2.THRESH_BINARY, blockSize=9, C=8)

plt.figure()
plt.imshow(adaptif_tresh_img, cmap="gray")
plt.axis("off")
plt.show()

