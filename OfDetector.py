import cv2
import numpy as np
import math

#-----------------------------
class OfDetector:
    def __init__(self):
        pass
    
    def detect(self, fpImg):
        #Detect Dimensions
        height, width = fpImg.shape

        #Calculate Gradient
        gx = cv2.Sobel(fpImg, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(fpImg, cv2.CV_32F, 0, 1)

        #Var. Init.
        orientation = 0
        sum1 = 0
        sum2 = 1
        of = np.zeros((16,16))

        for row in range(0,width, 16):
            for col in range(0,height, 16):
                tmp = []
                for i in range(row, row + 16):
                    for j in range(col, col + 16): 
                        sum1 += 2 * gx[i,j] * gy[i,j]
                        sum2 += (gx[i,j] ** 2) - (gy[i,j] ** 2)
                orientation = 0.5 * math.atan(sum1 / sum2)     
                orientation = math.degrees(orientation)
                of[row//16,col//16] = orientation+90

        return of
        
#-----------------------------
if __name__ == "__main__":
    pass
##    inpImg = cv2.imread("img/1_1.BMP", cv2.IMREAD_GRAYSCALE)
##    ofDetect = OfDetector()
##    temp = ofDetect.detect(inpImg)
##    height, width = inpImg.shape
##    print(temp)
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------


