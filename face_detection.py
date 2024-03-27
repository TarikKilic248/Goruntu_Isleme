# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:36:51 2024

@author: batma
"""

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()

mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = faceDetection.process(imgRGB)
    
    print(results.detections)
    
    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            
            h, w, _ = img.shape
            bbox = int(bboxC.xmin*w), int(bboxC.ymin*h), int(bboxC.width*w), int(bboxC.height*h)
            
            cv2.rectangle(img, bbox, (0,255,255), 2)
             
    
    
    
    
    if cv2.waitKey(1)&0xFF == ord('q'): break
    img_resized = cv2.resize(img, (840,550))
    cv2.imshow("img", img_resized)
    cv2.waitKey(1)
    
cap.release()
cv2.destroyAllWindows()