from box_detection import box_extraction
from KrakenizeBox import KrakenizeBox
from LineRemover import markVertical,cluster,average,main,crop, cropHeader
import cv2 as cv
from CleanOutput import Clean
from kraken import binarization
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np


def ExtractKK(path):
    img = cv.imread(path)
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # im_pil1 = Image.fromarray(img)
    # img = im_pil1
    # result1 = binarization.nlbin(img)                          Binarize for header only
    # rgb_im1 = result1.convert('RGB')
    # img = np.array(rgb_im1)

    table1, table2 = box_extraction(path)
    
    krtable1, krtable2 = KrakenizeBox(table1, table2)
    name = 1
    x1, height1, y1 = markVertical(krtable1)
    x2, height2, y2 = markVertical(krtable2)
    groupedX1 = cluster(x1,10)
    groupedX2 = cluster(x2,10)

    xPoints1 = average(groupedX1)
    xPoints2 = average(groupedX2)
 
    imageToBeCropped1 = main(krtable1)
    imageToBeCropped2 = main(krtable2)

    textHeader = cropHeader(xPoints1, y1,img, 0.75)
    text1 = crop(xPoints1, height1,imageToBeCropped1, 0.25)
    text2 = crop(xPoints2, height2, imageToBeCropped2, 0.25)


    print(textHeader)


    rawText = text1 + text2
    Clean(rawText)

ExtractKK('kartu-keluarga.jpeg')
