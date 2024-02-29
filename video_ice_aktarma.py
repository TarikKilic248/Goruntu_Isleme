import cv2 
import time

#video ice aktarma
video_name = "kill.mp4"

cap = cv2.VideoCapture(video_name)
print("Weight:", cap.get(3))
print("Height:", cap.get(4))

if cap.isOpened() == False:
    print("Hata, Video açılamadı.")
    

while True:
    ret, frame = cap.read()
    if ret != True:
        print("Video okumada hata var")
        break
    

    time.sleep(0.01)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release() #stop capture
cv2.destroyAllWindows()