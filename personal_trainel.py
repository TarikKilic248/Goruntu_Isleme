# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:43:08 2024

@author: batma
"""

import cv2
import mediapipe as mp
import numpy as np
import math
import time

def findAngle(img, p1, p2, p3, lmList, draw = True):
    #noktalarin x ve y kordinantlari
    x1, y1 = lmList[p1][1:]
    x2, y2 = lmList[p2][1:]
    x3, y3 = lmList[p3][1:]
    
    #aci hesapla
    angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
    if angle < 0 : angle += 360
    
    if draw:
        cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 3)
        cv2.line(img, (x3, y3), (x2, y2), (0,0,255), 3)
        
        cv2.circle(img, (x1, y1), 10, (0,255,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (0,255,255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 10, (0,255,255), cv2.FILLED)
        
        cv2.circle(img, (x1, y1), 10, (0,255,255))
        cv2.circle(img, (x2, y2), 10, (0,255,255))
        cv2.circle(img, (x3, y3), 10, (0,255,255))
    
        cv2.putText(img, str(int(angle)), (x2 - 40, y2 + 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 2)
        
    return angle
        
    

cap = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

dir = 0
count = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = pose.process(imgRGB)
    
    lmList = []
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,
                              mpPose.POSE_CONNECTIONS)
        
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            lmList.append([id, cx, cy])
    
    print(lmList)
    
    if len(lmList) != 0:
        #sinav
        angle = findAngle(img, 11, 13, 15, lmList)
        per = np.interp(angle, (50, 150), (0, 100))
        print(angle)
        
        
        if per == 100:
            if dir == 0:
                #egildi
                count += 0.5
                dir = 1
    
        if per == 0:
            if dir == 1:
                #egildi
                count += 0.5
                dir = 0
        
        print(count)
        
        cv2.putText(img, str(count), (45, 125),
                    cv2.FONT_HERSHEY_PLAIN, 5, (255,200,25), 4)
    
    
    #FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS: " + str(int(fps)), (410,75),
                cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
    
    
    if cv2.waitKey(1)&0xFF == ord('q'): break
    #img_resized = cv2.resize(img, (800,550))
    cv2.imshow("img", img)
    cv2.waitKey(1)
    
    
cap.release()
cv2.destroyAllWindows()
