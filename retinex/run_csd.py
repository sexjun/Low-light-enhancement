import sys
import os

import cv2
import json

import retinex

with open('config.json', 'r') as f:
    config = json.load(f)


img = cv2.imread("../cds_arithmetic/data/src/8.jpg")
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_NEAREST)

img_msrcr = retinex.MSRCR(
    img,
    config['sigma_list'],
    config['G'],
    config['b'],
    config['alpha'],
    config['beta'],
    config['low_clip'],
    config['high_clip']
)

img_amsrcr = retinex.automatedMSRCR(
    img,
    config['sigma_list']
)

img_msrcp = retinex.MSRCP(
    img,
    config['sigma_list'],
    config['low_clip'],
    config['high_clip']
)

shape = img.shape
cv2.imshow('Image', img)
cv2.imshow('retinex', img_msrcr)
cv2.imshow('Automated_retinex', img_amsrcr)
cv2.imshow('MSRCP', img_msrcp)
print("done")
cv2.waitKey(0)
cv2.destroyAllWindows()
print("eeeee")
