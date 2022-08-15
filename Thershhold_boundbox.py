import cv2
import numpy as np
from cv2 import cvtColor
import os
import glob
import glob
import cv2 as cv



path = glob.glob('.../*.jpg')

i= 0

for images in path:
    

    image = cv.imread(images)
    gray_img= cvtColor(image, cv2.COLOR_BGR2GRAY) # Gray-scaling the original image
    resized_img= cv2.resize(gray_img , (450,300)) # resizing the Gray-scaled image
    ret, binary_img = cv2.threshold(resized_img,127,255,cv2.THRESH_BINARY) # binary image of the Gray-scaled image
    contours, hierarchy = cv2.findContours(image=binary_img, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    
    detect_contour= cv2.drawContours(image, contours=contours, contourIdx=-1, color=(0,255, 0), thickness=2, lineType=cv2.LINE_AA)

    if i<= 0:
         os.makedirs('image_data/Results')


    for j in contours:
        x,y,w,h = cv2.boundingRect(j)
        if (8000<=x*w):
            final_result= cv2.rectangle(image, (x,y), (x+w, y+h), color=(255,0,0)  , thickness=2)
        if(1500<x*w <1700 ):
            final_result= cv2.rectangle(image, (x,y), (x+w, y+h), color=(255,0,0)  , thickness=1)


        
    i +=1
    cv2.imwrite(".../Image-%i.jpg" %i,final_result)
    # cv2.imwrite(".../Image-%0i.jpg" %i,gray_img)
    # cv2.imwrite(".../Image-%0i.jpg" %i,binary_img)

    
    cv2.imshow('Contour', final_result)
    cv2.waitKey(750)

cv2.destroyAllWindows()



# cv2.imshow('Binary image', bw_img)
# cv2.imshow('Resized', resized)
# cv2.imshow('Gray level image', gray_img)
# cv2.waitKey(0)
