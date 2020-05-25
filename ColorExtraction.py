import cv2
#import image
img = cv2.imread('dataset/0012_0001.jpg')
#resize image
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height) 
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
#show resized original img
cv2.imshow('Hello World', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
#show lab space
lab = cv2.cvtColor(resized,cv2.COLOR_BGR2LAB)
cv2.imshow("l*a*b",lab)
#show seperate lab space
L,A,B=cv2.split(lab)
cv2.imshow("L_Channel",L) # For L Channel
cv2.imshow("A_Channel",A) # For A Channel (Here's what You need)
cv2.imshow("B_Channel",B) # For B Channel
cv2.waitKey(0)
cv2.destroyAllWindows()
#split bgr
b,g,r=cv2.split(resized)
#merge agr
agr = cv2.merge([b,g,B])
cv2.imshow("agr",agr)
cv2.waitKey(0)
cv2.destroyAllWindows()