import cv2
import numpy as np

src = cv2.imread('D:\\tesseract\\OpenCVTest\\yinhangka.jpg')  # a black objects on white image is better


src_edge = cv2.medianBlur(src, 5)

result = cv2.Canny(src_edge, 100, 150, 3)

#contours, thresh = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(result, contours, -1, (255, 0, 0), 10)
# 显示图像
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.resizeWindow("result", 300, 400)
cv2.moveWindow("result", 200, 100)
cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()