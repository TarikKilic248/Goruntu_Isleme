# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:43:41 2024

@author: batma
"""

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("taken.png")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("doctor.png")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print("1. resim", img1.shape, "2. resim", img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

img1 = cv2.resize(img1, ( 600,600))
img2 = cv2.resize(img2, ( 600,600))

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karistirma remis = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)







