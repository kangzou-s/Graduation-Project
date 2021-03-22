# This script should take an image of the unsolved puzzle from ./puzzle_generator
# and output N smaller images, each containing one piece to folder ./segmented
import copy
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt #import function library which will be used 

#part1 Pretreatment
pattern = cv.imread('./segmented/piece_2.png')


pattern = (0.3*pattern[:,:,2] + 0.6*pattern[:,:,1] + 0.1*pattern[:,:,0]).astype(np.uint8)
pattern = 255 * (pattern > 5 ).astype(np.uint8)


contours, _ = cv.findContours(pattern, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
mask = np.ones(pattern.shape, dtype=np.uint8)*255
print('Contour lengths: ', [len(i) for i in contours])
cv.drawContours(mask, contours, -1, (0,0,0), thickness=cv.FILLED)
cv.imshow('',mask)
cv.waitKey(0)


rect = cv.minAreaRect(contours)
print(rect[0])
print(rect[1])
print(rect[2])
box=cv.boxPoint(rect)
box=np.int0(box)
cv.drawContours(pattern,[box],0,(0,0,255),2)

cv.imshow('',pattern)
cv.waitKey(0)



