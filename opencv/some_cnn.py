import cv2 as cv
import numpy as np


def blur_demo(image):#均值模糊
    dst = cv.blur(image,(5,5))
    cv.imshow("blur",dst)
    #cv.imwrite("/home/lym/pic/test_blur_cnn.jpg",dst)


def medianBlur_demo(image):#均值模糊
    dst = cv.medianBlur(image,5)
    cv.imshow("blur",dst)
    cv.imwrite("/home/lym/pic/test_median_cnn.jpg",dst)



print("-----------------------------Hello Python----------------------------------")
src = cv.imread("/home/lym/test.jpg")
cv.namedWindow("input_image",cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)
medianBlur_demo(src)


cv.waitKey(0)

cv.destroyAllWindows()