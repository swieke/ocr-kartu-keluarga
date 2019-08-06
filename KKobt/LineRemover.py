import numpy as np
import cv2 as cv
import os
from itertools import groupby
import pytesseract

def markVertical(path):
    src = path
    height, width = src.shape[:2]

    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src

    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, -2)

    horizontal = np.copy(bw)
    vertical = np.copy(bw)

    cols = horizontal.shape[1]
    horizontal_size = int(cols / 30)

    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))
    horizontal = cv.erode(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, horizontalStructure)

    #np.set_printoptions(threshold=np.inf)


    h_transpose = np.transpose(np.nonzero(horizontal))

  


    rows = vertical.shape[0]
    verticalsize = int(rows / 30)
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)



    v_transpose = np.transpose(np.nonzero(vertical))

    img = src.copy()

    minLineLength = 100
    maxLineGap = 200
    lines = cv.HoughLinesP(vertical,1,np.pi/180,100,minLineLength,maxLineGap)
    x = []
    y = []
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            x.append(x1)
            y.append(y1)
    
    return x, height, y


def cluster(data, maxgap):
    '''Arrange data into groups where successive elements
       differ by no more than *maxgap*

        >>> cluster([1, 6, 9, 100, 102, 105, 109, 134, 139], maxgap=10)
        [[1, 6, 9], [100, 102, 105, 109], [134, 139]]

        >>> cluster([1, 6, 9, 99, 100, 102, 105, 134, 139, 141], maxgap=10)
        [[1, 6, 9], [99, 100, 102, 105], [134, 139, 141]]

    '''
    data.sort()
    groups = [[data[0]]]
    for x in data[1:]:
        if abs(x - groups[-1][-1]) <= maxgap:
            groups[-1].append(x)
        else:
            groups.append([x])
    return groups


def main(argv):
    kernel = np.ones((8,8), np.uint8)
    src = argv
   
    cv.imshow("src", src)
    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src
 
    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)

    horizontal = np.copy(bw)
    vertical = np.copy(bw)

    cols = horizontal.shape[1]
    horizontal_size = cols // 20

    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

    horizontal = cv.erode(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, kernel)

    new = bw - horizontal

    rows = vertical.shape[0]
    verticalsize = rows // 20

    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))
    # Apply morphology operations
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)
    vertical = cv.dilate(vertical, kernel)
 
    new = new - vertical
          
    return (255-new)



def average(input):
    xPoints = []
    for similarValues in input:
        avg = lambda x,y: x/y
        averageX = int(avg(sum(similarValues),len(similarValues)))
        xPoints.append(averageX)
    return xPoints


name = 1
def crop(xp,height,image,ratio):
    idx = 1
    global name
    textHeader = ''
    text = ''
    while idx < (len(xp)-1):
        # print(idx)
        new_img = image[int(ratio*height):height-10, xp[idx]+5:xp[idx+1]]
        cv.imwrite(str(name)+'.jpg',new_img)
        text += pytesseract.image_to_string(new_img, lang="ind", config='--psm 11 --oem 3') +'\n'
        idx += 1
        name+= 1

    return text


def cropHeader(xp,height,image,ratio):
    idx = 1
    global name

    text = ''
    
    new_img = image[0:int(ratio * height[0]), xp[0]:xp[9]]
    cv.imwrite('header.jpg',new_img)
    text += pytesseract.image_to_string(new_img, lang="ocr", config='--psm 11 --oem 3') +'\n'
    idx += 1
    name+= 1

    return text
