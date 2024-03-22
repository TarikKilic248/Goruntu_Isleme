# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:55:45 2024

@author: batma
"""

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils

tipIds = [4,8,12,16,20]
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    lmList = []
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms,
                                  mpHand.HAND_CONNECTIONS)
            
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                
                #if id == 8:
                #    cv2.circle(img, (cx, cy), 9, (255,0,0), cv2.FILLED)
                #    
                #if id == 6:
                #    cv2.circle(img, (cx, cy), 9, (0,255,0), cv2.FILLED)
                
    #print(lmList)
            
    if len(lmList) != 0:
        fingers = []
        
        #bas parmak
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
            
        #4 parmak
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
            #print(fingers)
            
        totallF = (fingers.count(1)) + 1
        print(totallF)
            
        cv2.putText(img, str(totallF), (10,75),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
                                             
    
    
    
    
    
    
    if cv2.waitKey(1)&0xFF == ord('q'): break
    
    cv2.imshow("img", img)
    cv2.waitKey(1)
    
cap.release()
cv2.destroyAllWindows()