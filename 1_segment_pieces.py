# This script should take an image of the unsolved puzzle from ./puzzle_generator
# and output N smaller images, each containing one piece to folder ./segmented
import copy
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt #import function library which will be used 

# Load pattern
pattern = cv.imread('/Users/qinghuan/Desktop/task1/4x4.jpg')
# Make grayscale and make type conversion
pattern = (0.3*pattern[:,:,2] + 0.6*pattern[:,:,1] + 0.1*pattern[:,:,0]).astype(np.uint8)
# Threshold
pattern = 255 * (pattern > 225).astype(np.uint8)


contours, _ = cv.findContours(pattern, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #find Contour
print('Contour lengths: ', [len(i) for i in contours])      #print the lengths of contour

res = np.ones(pattern.shape, dtype=np.uint8) * 255。        #Make a white curtain
cv.drawContours(res, contours, -1, (100,100,100), thickness=cv.FILLED)  #draw contour

# Load image and cut into puzzles
img = cv.imread('/Users/qinghuan/Desktop/task1/godzilla.jpg')    
img_cols, img_rows = img.shape[:2]
pat_cols, pat_rows = pattern.shape[:2]      #get size

img = cv.resize(img, None, fy = pat_cols/img_cols, fx = pat_rows/img_rows) #size convert
img = (0.3*img[:,:,2] + 0.6*img[:,:,1] + 0.1*img[:,:,0]).astype(np.uint8) # Convert to grayscale
img = np.stack( (img, img, img, 255*np.ones(img.shape, dtype=np.uint8)) , axis=2) # Get back to color, for alpha channel. change from jpg to png

# Cut pieces
pieces = []
for i in range(len(contours)):
	mask = np.ones(pattern.shape, dtype=np.uint8)*255
	cv.drawContours(mask, contours, i, (0,0,0), thickness=cv.FILLED)  #for every contour, draw it 

	piece = copy.deepcopy(img)   #creat a new jpg to avoid inflect the original ipg
	piece[mask > 0,:] = 0
	
	x,y,w,h = cv.boundingRect(contours[i]) #use a minimal rectangle to contain the contour
	print(x, y, w, h)
	pieces.append(piece[y:y+h, x:x+w])

side = np.ceil(np.sqrt(len(pieces)))    #get the nunber of how many pieces we have 
for i in range(len(pieces)):
	plt.subplot(side, side, i+1), plt.imshow(pieces[i])  #draw all the pieces we get
	cv.imwrite('piece_'+str(i)+'.png', pieces[i])    #save piece we get
	
plt.show()
	
