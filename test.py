import cv2
import numpy
import os

os.getcwd()

a = numpy.array([3,5])

img = cv2.imread('./Pictures/python.png', cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ', img.shape)

scale_percent = 200  # percent of original size
x = img.shape[1]*0.6
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)
cv2.namedWindow('Resized image', cv2.WINDOW_NORMAL)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('lena.jpg')
