# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:48:06 2024

@author: batma
"""

import cv2
import mediapipe as mp
import time

pTime = 0
cTime = 0

mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture("snipwhow.mp4")

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,
                              mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            
            if id == 4:
                cv2.circle(img, (cx, cy), 5, (255,0,0), cv2.FILLED)
        
    #FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS: " + str(int(fps)), (10,75),
                cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
    
    if cv2.waitKey(1)&0xFF == ord('q'): break
    img_resized = cv2.resize(img, (800,550))
    cv2.imshow("img", img_resized)
    cv2.waitKey(1)
    
cap.release()
cv2.destroyAllWindows()

