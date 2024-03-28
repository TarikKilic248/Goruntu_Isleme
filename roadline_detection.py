# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:41:52 2024

@author: batma
"""

import cv2
import time
import numpy as np

cap = cv2.VideoCapture("golovach.mp4")

pTime = 0
cTime = 0

def process(image):
    height, width = img.shape[0], img.shape[1]
    
    region_of_interest_vertices = [(250, height-150), (width/2, (height/2)-400),
                                   (width-250, height-150)]
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, 250, 120)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    
    #↑maskeleme yaptigimiz yer icin islem
    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi/180, threshold=220,
                    lines=np.array([]), minLineLength=150, maxLineGap=2)
    print(lines)
    if lines is not None:
        imageWithLine = drawLines(image, lines)
    else:
    # Çizgi bulunamadığında yapılacak işlemleri burada tanımlayabilirsiniz
        print("No lines detected!")
        imageWithLine = image
    
    return imageWithLine


def drawLines(image, lines):
    image = np.copy(image)
    blank_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0,255,0), thickness=10)
            
    image = cv2.addWeighted(image, 0.8, blank_image, 1, 0.0)
    
    return image
    
    


def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255
    
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    
    return masked_image

while True:
    success, img = cap.read()
    img = process(img)
    if success:
    
    

    
        #FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, "FPS: " + str(int(fps)), (410,75),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
        
        
        if cv2.waitKey(1)&0xFF == ord('q'): break
        img_resized = cv2.resize(img, (840,550))
        cv2.imshow("img", img_resized)
        cv2.waitKey(1)
    else:
        break
    
cap.release()
cv2.destroyAllWindows()