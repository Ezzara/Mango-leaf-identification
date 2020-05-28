#importing array of image
import cv2
from sklearn.neighbors import KNeighborsClassifier as KNN
import numpy as np
import glob
#function to import bunch of image from folder, its returning tuple of image
def import_image (files):
    X_data = []
    for myFile in files:
        image = cv2.imread (myFile)
        #resize
        scale_percent = 10 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height) 
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        hist,bins = np.histogram(resized,256,[0,256])
        hist = np.transpose(hist[0:18,np.newaxis])
        #append resized image
        X_data.append(hist)
    return X_data


#X_data = []

files_training = glob.glob ("dataset/*.jpg")
X_data = import_image(files_training)
files_testing = glob.glob ("datatraining/*.jpg")
X_testing = import_image(files_testing)

'''
for myFile in files:
    image = cv2.imread (myFile)
    #resize
    scale_percent = 10 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height) 
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    hist,bins = np.histogram(resized,256,[0,256])
    hist = np.transpose(hist[0:18,np.newaxis])
    #append resized image
    X_data.append(hist)
    '''
'''
#to test the imported image    
cv2.imshow('Hello World', X_data[1])
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
#class of data training
response = np.array([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]).astype(np.float32)
#convert to 1d array
datafin = np.concatenate((X_data[:]),axis=0)
datatest = np.concatenate((X_testing[:]),axis=0)
#KNN
knn = KNN(n_neighbors=2, weights="uniform")
knn.fit(datafin,response)
#testing
res = knn.predict(datatest)
print(res)
