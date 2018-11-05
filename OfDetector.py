import cv2
import numpy as np
import math

SIZE = 16
#-----------------------------
class OfDetector:
    def __init__(self):
        pass
    
    def findOrientationBlock(self, block):
        gx = cv2.Sobel(block, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(block, cv2.CV_32F, 0, 1)

        sum1 = 0
        sum2 = 0

        for blockW in range(0,SIZE):
            for blockC in range(0,SIZE):
                sum1+=2*gx[blockW, blockC] * gy[blockW, blockC]
                sum2+=(gx[blockW, blockC])**2 - (gy[blockW, blockC])**2
                
        orientation = (np.arctan2(sum1, sum2) * 0.5)
        orientation = (orientation + np.pi * 0.5) % np.pi

        return math.degrees(orientation)+45
    
    def detect(self, fpImg):
        #Detect Dimensions
        height, width = fpImg.shape

        #Var. Init.
        of = np.zeros((SIZE,SIZE), dtype=np.float32)

        for row in range(0,width, SIZE):
            for col in range(0,height, SIZE):
                block = fpImg[row:row+SIZE, col:col+SIZE]
                temp = self.findOrientationBlock(block)
                of[row // SIZE, col // SIZE] = self.quantize(temp)
                
        print(of)
        return of

    def quantize(self, degrees):
        if(degrees < 0):
            degrees = degrees + 360
        if(degrees > 180):
            degrees = degrees / 2
        if(degrees > 0 and degrees < 22.5):
            return 0.0
        elif(degrees >= 22.5 and degrees < 45):
            return 22.5
        elif(degrees >= 45 and degrees < 67.5):
            return 45.0
        elif(degrees >= 67.5 and degrees < 90):
            return 67.5
        elif(degrees >= 90 and degrees < 112.5):
            return 90.0
        elif(degrees >= 112.5 and degrees < 135):
            return 112.5
        elif(degrees >= 135 and degrees < 157.5):
            return 135.0
        elif(degrees >=157.5 and degrees < 180):
            return 157.5
        
#-----------------------------
if __name__ == "__main__":
    ##pass
    inpImg = cv2.imread("img/1_1.BMP", cv2.IMREAD_GRAYSCALE)
    ofDetect = OfDetector()
    temp = ofDetect.detect(inpImg)
    print(len(temp))
    height, width = inpImg.shape
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------


