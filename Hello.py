from matplotlib import pyplot as plt
import cv2
src = cv2.imread("D:\\tesseract\\51.jpg")

src_edge = cv2.GaussianBlur(src, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
src_gray = cv2.cvtColor(src_edge,  cv2.COLOR_BGR2GRAY)
result = cv2.Laplacian(src_gray, cv2.CV_16S, 3)
result1 = cv2.convertScaleAbs(result)
cv2.namedWindow('enhanced', cv2.WINDOW_NORMAL)
cv2.resizeWindow("enhanced", 300, 400)
cv2.moveWindow("enhanced", 200, 100)
cv2.imshow("enhanced", src_edge)
cv2.waitKey(0)