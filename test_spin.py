# This script should take an image of the unsolved puzzle from ./puzzle_generator
# and output N smaller images, each containing one piece to folder ./segmented
import copy
import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt #import function library which will be used 

#part1 Pretreatment
pattern = cv.imread('./segmented/piece_2.png')
rows,cols=pattern.shape[0:2]
print(rows)
print(cols)

pattern = (0.3*pattern[:,:,2] + 0.6*pattern[:,:,1] + 0.1*pattern[:,:,0]).astype(np.uint8)
pattern = 255 * (pattern > 5 ).astype(np.uint8)
'''cv.imshow('',pattern)
cv.waitKey(0)'''


contours, _ = cv.findContours(pattern, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(contours[0])
contours = [list(map(float,point[0])) for point in contours[0]]
for i in range(len(contours)):
	contours[i][0] = math.atan((contours[i][0]-rows/2))
	contours[i][1] = (contours[i][1]-cols/2)	

coor1= contours
coor = contours
a=len(coor)
phi=np.ones([1,len(coor)],dtype=np.float)
rho=np.ones([1,len(coor)],dtype=np.float)
for i in range(len(coor)): 
	if coor[i][1]>=0:
		coor[i][0]=(coor1[i][0]/coor1[i][1])
		coor[i][1]=math.sqrt(math.pow(coor1[i][0],2)+math.pow(coor1[i][1],2))
	else:
		coor[i][0]=(coor1[i][0]/coor1[i][1]) + math.pi
		coor[i][1]=math.sqrt(math.pow(coor1[i][0],2)+math.pow(coor1[i][1],2))
	phi[0][i] = coor[i][0]
	rho[0][i] = coor[i][1]
print(phi)
print(rho)
plt.plot(phi[0],rho[0])
plt.title('graph of contours in (phi,rho)')
plt.show()




