from kraken import binarization
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

def KrakenizeBox(img1, img2):
    image1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
    im_pil1 = Image.fromarray(image1)
    image1 = im_pil1

    image2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
    im_pil2 = Image.fromarray(image2)
    image2 = im_pil2

    result1 = binarization.nlbin(image1)
    result2 = binarization.nlbin(image2)
    
    rgb_im1 = result1.convert('RGB')
    rgb_im2 = result2.convert('RGB')

    open_cv_image1 = np.array(rgb_im1)
    open_cv_image2 = np.array(rgb_im2)

    return open_cv_image1, open_cv_image2