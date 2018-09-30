import cv2 as cv
import numpy as np
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]

    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)

    # 执行旋转
    M = cv.getRotationMatrix2D(center, angle, scale)
    rotated = cv.warpAffine(image, M, (w, h))

    # 返回旋转后的图像
    return rotated

print("-----------------------------Hello Python----------------------------------")
src = cv.imread("2222.jpg")
#gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.namedWindow("input_image",cv.WINDOW_AUTOSIZE)
cv.imshow("input_image",src)
#cv.imshow("input_image",gray)
print(src.shape)
part_of = src[50:1600,100:1700]

rotated = rotate(part_of, 100)
cv.imshow("Rotated by 45 Degrees", rotated)

cv.imwrite("/home/lym/pic/65_160_Degress.jpg",rotated)
'''
rotated = rotate(image, -45)
cv2.imshow("Rotated by -45 Degrees", rotated)
rotated = rotate(image, 90)
cv2.imshow("Rotated by 90 Degrees", rotated)
rotated = rotate(image, -90)
cv2.imshow("Rotated by -90 Degrees", rotated)
rotated = rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
'''

#gray = cv.cvtColor(part_of,cv.COLOR_BGR2GRAY)
#BACKFace = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
#src[300:1000,0:1500] = BACKFace
cv.namedWindow("part",cv.WINDOW_AUTOSIZE)
cv.imshow("part",part_of)
cv.imwrite("1186.jpg",rotated)

cv.waitKey(0)

cv.destroyAllWindows()