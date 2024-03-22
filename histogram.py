# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:44:42 2024

@author: batma
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("doctor.png")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img_vis)

print(img.shape)

#histogram
img_hist = cv2.calcHist(img, channels= [0], mask= None,
                        histSize= [256], ranges=[0,256])

print(img_hist.shape)
plt.figure()
plt.plot(img_hist)

color = ("b", "g", "r")
plt.figure()
for i, c in enumerate(color):
    img_hist = cv2.calcHist(img, channels= [i], mask= None,
                            histSize= [256], ranges=[0,256])
    plt.plot(img_hist, color = c)

    