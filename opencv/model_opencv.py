import cv2 as cv



print("-----------------------------Hello Python----------------------------------")
src = cv.imread("/home/lym/test.jpg")
cv.namedWindow("input_image",cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)



cv.waitKey(0)

cv.destroyAllWindows()