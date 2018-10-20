import cv2
import pyautogui
import numpy as np

cap = cv2.VideoCapture(0)
# PINK_MIN = np.array([120, 50, 50], np.uint8) #change
# PINK_MAX = np.array([180, 180, 200], np.uint8)
BLUE_MIN = np.array([110,100,100])
BLUE_MAX = np.array([130,255,255])
centroid_x = 0
centroid_y = 0
s = ''
move = ''
pyautogui.FAILSAFE = False

while(cap.isOpened()):

    ret, img = cap.read()
    img = cv2.flip(img, 1)

    #thresh = cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)
    orig = cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    #img = cv2.GaussianBlur(img, (15, 15), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

    frame_threshed = cv2.inRange(hsv, BLUE_MIN, BLUE_MAX) #change

    _,contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)
    max_area = 0
    last_x = centroid_x
    last_y = centroid_y

    if contours:
        for i in contours:
            area = cv2.contourArea(i)
            if area > max_area:
                max_area = area
                cnt = i

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        centroid_x = (x + x+w)/2
        centroid_y = (y + y+h)/2

        cv2.circle(img, (centroid_x, centroid_y), 2, (0,0,255), 2)
        cv2.line(img,(250,0),(250,700),(255,0,0),5)
        cv2.line(img,(400,0),(400,700),(255,0,0),5)
        cv2.line(img,(250,150),(400, 150),(255,0,0),5)
        cv2.line(img,(250,350),(400, 350),(255,0,0),5)

        #cv2.imshow('Threshold', frame_threshed)
        cv2.imshow('Original', img)

        pyautogui.dragTo(centroid_x, centroid_y, duration=0) 
        

    k = cv2.waitKey(10)
    if k == 27:
        break
