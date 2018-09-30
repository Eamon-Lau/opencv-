import cv2 as cv
import numpy as np
'''
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s, channels : %s"%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixel_demo",image)
'''

def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse_demo",dst)



src = cv.imread("/home/lym/test.jpg")
cv.namedWindow("input_image",cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)
#___________________________________________________________________________________________
t1 = cv.getTickCount()
#access_pixels(src)
inverse(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time : %s s"%(time*1000))
#___________________________________________________________________________________________time cost
cv.waitKey(0)