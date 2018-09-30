import cv2 as cv
import numpy as np

def creat_image():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    cv.imshow("new_image",img)
    cv.imwrite("/home/lym/pic/aaa.jpg",img)

creat_image()
src = cv.imread("/home/lym/test.jpg")
cv.namedWindow("input_image",cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)
creat_image()
cv.waitKey(0)