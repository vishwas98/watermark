#!/usr/bin/env python
# coding: utf-8




import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread('F:/Vishwas.jpeg' )// load the image you want to watermark
img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)// convert to rgb
plt.imshow(img_rgb);//display of image
print('image dtype ',img_rgb.dtype)
blank_img = np.zeros(shape=(img_rgb.shape[0],img_rgb.shape[1],3), dtype=np.uint8)
font = cv2.FONT_HERSHEY_PLAIN  // font and attributes of the watermark
cv2.putText(blank_img,  
            text='Getty image',  
            org=(10,120),   
            fontFace=font,  
            fontScale= 1,color=(255,255,255),  
            thickness=1,  
            lineType=cv2.LINE_AA)  
plt.imshow(blank_img); // display the watermark needed to apply on the image
blended = cv2.addWeighted(src1=img_rgb,alpha=0.7,src2=blank_img,beta=1, gamma = 0) //combine the two images
plt.imshow(blended);//display of watermarked image





