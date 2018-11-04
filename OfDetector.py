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
                of[row//16,col//16] = self.quantize(orientation+90)
        
        return of

    def quantize(self, degrees):
        if(degrees > 0 and degrees < 22.5):
            return 0.0
        elif(degrees >= 22.5 and degrees < 45):
            return 22.5
        elif(degrees >= 45 and degrees < 67.5):
            return 45.0
        elif(degrees >= 67.5 and degrees < 90):
            return 67.5
        elif(degrees >= 90 and degrees < 112.5):
            return 90
        elif(degrees >= 112.5 and degrees < 135):
            return 112.5
        elif(degrees >= 135 and degrees < 157.5):
            return 135.0
        elif(degrees >=157.5 and degrees < 180):
            return 157.5
        else:
            return None
        
#-----------------------------
if __name__ == "__main__":
    ##pass
    inpImg = cv2.imread("img/1_1.BMP", cv2.IMREAD_GRAYSCALE)
    ofDetect = OfDetector()
    temp = ofDetect.detect(inpImg)
    print(temp)
    height, width = inpImg.shape
    cv2.waitKey()
    cv2.destroyAllWindows()
ั
#-----------------------------


