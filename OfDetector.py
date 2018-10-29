import cv2
import numpy as np
import math

#-----------------------------
class OfDetector:
    def __init__(self):
        pass
    
    def detect(self, fpImg):
        
        height, width = fpImg.shape

        gx = cv2.Sobel(fpImg, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(fpImg, cv2.CV_32F, 0, 1)

        orientation = 0
        sum1 = 0
        sum2 = 0
        
        for row in range(0,width):
            for col in range(0,height):
                sum1 += 2 * gx[row,col] * gy[row,col]
                sum2 += (gx[row,col] ** 2) - (gy[row,col] ** 2)

        orientation = 0.5 * math.atan(sum1 / sum2)
        orientation = math.degrees(orientation)
        
        return orientation
        
#-----------------------------
if __name__ == "__main__":
    pass
##    inpImg = cv2.imread("img/1_1.BMP", cv2.IMREAD_GRAYSCALE)
##    ofDetect = OfDetector()
##    absGx, absGy = ofDetect.detect(inpImg, inpImg)
##    cv2.imshow("absGx", absGx)
##    cv2.imshow("absGy", absGy)
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------


