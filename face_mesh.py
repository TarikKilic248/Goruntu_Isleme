# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:30:09 2024

@author: batma
"""

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

pTime = 0
cTime = 0

mpFaceMesh =  mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=3)

mpDraw = mp.solutions.drawing_utils
#mesh uzaktayken anlasilmadigi icin
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    
    print(results.multi_face_landmarks)
    
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            #mpFaceMesh.FACEMESH_TESSELATION mesh olusturmak icin
            #mpFaceMesh.FACEMESH_CONTOURS noktalama icin
            mpDraw.draw_landmarks(img, faceLms,
                                  mpFaceMesh.FACEMESH_TESSELATION,
                                  drawSpec, drawSpec)
            
            
        for id, lm in enumerate(faceLms.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            print([id, cx, cy])
            
    
    
    

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
    
cap.release()
cv2.destroyAllWindows()