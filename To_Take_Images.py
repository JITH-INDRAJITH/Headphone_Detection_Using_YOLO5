import cv2
import time
cpt = 0
maxFrames = 45
cap=cv2.VideoCapture(0)
while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    cv2.imshow("test window", frame)
    cv2.imwrite("C:/Users/HP/Desktop/headphone_detection/headphone/images/Person_without_headphone_%d.jpg" %cpt, frame)
    #cv2.imwrite("C:/Users/HP/Desktop/headphone_detection/headphone/images/Person_with_headphone_%d.jpg" %cpt, frame)  ##This one for person with headphones
    
    time.sleep(0.5)
    cpt += 1
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()