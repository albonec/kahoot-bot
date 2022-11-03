import numpy as np
import cv2
from mss import mss

sct = mss()
bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

def detect_color(hMin, hMax, sMin, sMax, vMin, vMax):
    img = np.array(sct.grab(bounding_box))
    imgFiltered = cv2.bitwise_and(img, img, mask=cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array([hMin, sMin, vMin]), np.array([hMax, sMax, vMax])))
    imgCanny = cv2.Canny(imgFiltered, 50, 50)
    cv2.imshow("canny", imgCanny)
    cv2.waitKey(1)


while True:
    detect_color(0, 0, 90, 110, 36, 56)
