import cv2
import numpy as np
import math

SIZE = 16
#-----------------------------
class OfDetector:
    def __init__(self):
        self.original = []
        self.of = []
    
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

        return math.degrees(orientation)+45, math.degrees(orientation) 
    
    def detect(self, fpImg):
        #Detect Dimensions
        height, width = fpImg.shape

        #Var. Init.
        self.original = np.zeros((SIZE,SIZE), dtype=np.float32)
        self.of = np.zeros((SIZE,SIZE), dtype=np.float32)
        self.ofMat = np.zeros((SIZE,SIZE), dtype=np.float32)

        for row in range(0,width, SIZE):
            for col in range(0,height, SIZE):
                block = fpImg[row:row+SIZE, col:col+SIZE]
                temp, temp2 = self.findOrientationBlock(block)
                self.original[row // SIZE, col // SIZE] = temp2
                self.of[row // SIZE, col // SIZE] = self.quantize(temp)
                self.ofMat[row // SIZE, col // SIZE] = self.quantize(temp2)
                
        return self.of, self.ofMat, self.original

    def quantize(self, degrees):
        orList = [0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5]
        if degrees<0:
            degrees+=360
        if degrees>180:
            degrees/=2
        maxd = 180
        temp = 0
        for degree in orList:
            deg = abs(degree-degrees)
            if deg<maxd:
                maxd = deg
                temp = degree
        return temp
        
#-----------------------------
if __name__ == "__main__":
    pass
##    inpImg = cv2.imread("img/1_1.BMP", cv2.IMREAD_GRAYSCALE)
##    ofDetect = OfDetector()
##    temp = ofDetect.detect(inpImg)
##    print(len(temp))
##    height, width = inpImg.shape
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------


