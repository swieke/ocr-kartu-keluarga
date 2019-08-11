from box_detection import box_extraction
from KrakenizeBox import KrakenizeBox
from LineRemover import markVertical,cluster,average,main,crop, cropHeader
import cv2 as cv
from CleanOutput import Clean, CleanHeader, getKKNo
from kraken import binarization
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np


def ExtractKK(path):
    img = cv.imread(path)
    height, width = img.shape[:2]
    # Binarize
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    im_pil1 = Image.fromarray(img)
    img = im_pil1
    result1 = binarization.nlbin(img)                          
    rgb_im1 = result1.convert('RGB')
    img = np.array(rgb_im1)

    table1, table2, y2ForHeader = box_extraction(path)
    krtable1, krtable2 = KrakenizeBox(table1, table2)
    name = 1
    x1, height1, y1, width1 = markVertical(krtable1)

    y1.sort()
    y1 = cluster(y1,10)
    y1 = average(y1)
    # print(y1)

    x2, height2, y2, width2 = markVertical(krtable2)
    groupedX1 = cluster(x1,10)
    groupedX2 = cluster(x2,10)

    xPoints1 = average(groupedX1)
    xPoints2 = average(groupedX2)
 
    imageToBeCropped1 = main(krtable1)
    cv.imwrite('tabel1.jpg', imageToBeCropped1)
    imageToBeCropped2 = main(krtable2)
    cv.imwrite('tabel2.jpg', imageToBeCropped2)

    textHeader, textNo = cropHeader(xPoints1, y2ForHeader+5, img, 1, width) #height1
    text1 = crop(xPoints1, height1,imageToBeCropped1, 0.25)
    text2 = crop(xPoints2, height2, imageToBeCropped2, 0.25)


    # print(textHeader)
   
    rawText = text1 + text2
    Clean(rawText)
    CleanHeader(textHeader)
    getKKNo(textNo)



ExtractKK('kkkkk.jpg')


# kartu-keluarga.jpeg
# kkkkk.jpg ->
# kk3.png