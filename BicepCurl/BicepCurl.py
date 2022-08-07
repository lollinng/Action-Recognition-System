
from multiprocessing import Barrier
import cv2
import os
import sys
import numpy as np
import time
sys.path.insert(0, os.path.abspath(''))
from PoseNet import PoseModule as pm


cap = cv2.VideoCapture(0)

detector = pm.poseDetector()
count = 0
state = 0
while cap.isOpened():
    _, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len([lmList]) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        
        # Left Arm
        # angle = detector.findAngle(img, 11, 13, 15,False)


        # for regular dimensions
        # per = np.interp(-angle, (-165, -38),(0,100) )
        # bar = np.interp(angle, (38, 130), (200, 450))

        # for (1280, 720)
        per = np.interp(-angle, (-165, -40), (0, 100))
        bar = np.interp(angle, (40, 130), (100, 650))

        print(angle, per,bar)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if state == 0:
                count += 0.5
                state = 1
        if per == 0:
            color = (0, 255, 0)
            if state == 1:
                count += 0.5
                state = 0

        
        # for regular dimensions
        # # Draw Bar
        # cv2.rectangle(img, (500, 200), (620, 450), color,3 )
        # cv2.rectangle(img, (500, int(bar)), (620, 450), color,cv2.FILLED)
        # cv2.putText(img, f'{int(per)} %', (500, 75), cv2.FONT_HERSHEY_PLAIN, 4,
        #             color, 4)
        # # Rep data
        # cv2.rectangle(img, (0,0), (225,73), (245,117,16), -1)
        # cv2.putText(img, 'REPS', (15,12), 
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        # cv2.putText(img, str(count), 
        #             (10,60), 
        #             cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)


        # for (1280, 720)
        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)
 
        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)


    cv2.imshow('Mediapipe Feed', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
