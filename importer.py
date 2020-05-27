#importing array of image
import cv2
#import numpy as np
import glob

X_data = []
files = glob.glob ("dataset/*.jpg")
for myFile in files:
    image = cv2.imread (myFile)
    #resize
    scale_percent = 10 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height) 
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
    #append resized image
    X_data.append (resized)

'''
#to test the imported image    
cv2.imshow('Hello World', X_data[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
'''