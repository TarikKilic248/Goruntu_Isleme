# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:46:19 2024

@author: batma
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("tarik.png", 0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Original")


kernel = np.ones((5,5), dtype=np.uint8)

#erozyon
result = cv2.erode(img, kernel, iterations=1)
plt.figure()
plt.imshow(result, cmap="gray")
plt.axis("off")
plt.title("Erozyon")

#genisleme
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure()
plt.imshow(result2, cmap="gray")
plt.axis("off")
plt.title("Genisleme")

#white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise * 255

plt.figure()
plt.imshow(whiteNoise, cmap="gray")
plt.axis("off")
plt.title("whiteNoise")

noise_img = whiteNoise + img

plt.figure()
plt.imshow(noise_img, cmap="gray")
plt.axis("off")
plt.title("white noise with image")

#acilma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(opening, cmap="gray")
plt.axis("off")
plt.title("acilma")

#black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise * -255

plt.figure()
plt.imshow(blackNoise, cmap="gray")
plt.axis("off")
plt.title("blackNoise")

noise_img2 = blackNoise + img
noise_img2[noise_img2 <= -245] = 0

plt.figure()
plt.imshow(noise_img2, cmap="gray")
plt.axis("off")
plt.title("black noise with image")

#kapatma
closing = cv2.morphologyEx(noise_img2.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(closing, cmap="gray")
plt.axis("off")
plt.title("kapatma")

#gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient, cmap="gray")
plt.axis("off")
plt.title("gradient")















