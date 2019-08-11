import numpy as np
import cv2
im = cv2.imread('header.jpg')
im_ycrcb = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

ball_ycrcb_mint = np.array([0, 90, 100],np.uint8)
ball_ycrcb_maxt = np.array([25, 255, 255],np.uint8)
ball_ycrcb = cv2.inRange(im_ycrcb, ball_ycrcb_mint, ball_ycrcb_maxt)
#cv2.imwrite('Photos/output2.jpg', ball_ycrcb) # Second image
areaArray = []
count = 1

contours, _ = cv2.findContours(ball_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i, c in enumerate(contours):
    area = cv2.contourArea(c)
    areaArray.append(area)

#first sort the array by area
sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)

#find the nth largest contour [n-1][1], in this case 2
secondlargestcontour = sorteddata[1][1]

#draw it
x, y, w, h = cv2.boundingRect(secondlargestcontour)
cv2.drawContours(im, secondlargestcontour, -1, (255, 0, 0), 2)
cv2.rectangle(im, (x, y), (x+w, y+h), (0,255,0), 2)
cv2.imwrite('hasil.jpg', im)