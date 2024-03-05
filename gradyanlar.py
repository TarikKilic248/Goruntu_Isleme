# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:19:35 2024

@author: batma
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.png", 0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original")
plt.show()

#x gradyan
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx=1, dy=0, ksize=7)
plt.figure()
plt.imshow(sobelx, cmap="gray")
plt.axis("off")
plt.title("sobel x")
plt.show()

#x gradyan
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx=0, dy=1, ksize=7)
plt.figure()
plt.imshow(sobely, cmap="gray")
plt.axis("off")
plt.title("sobel y")
plt.show()

#Laplacian gradyan
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap="gray")
plt.axis("off")
plt.title("laplancian")
plt.show()