import cv2
import numpy as np
import math

#-----------------------------
class FpSegmentator:
    def __init__(self, bs = 16):
        self.blockSize = bs
        
    def segment(self, fpImg):  
        print("Stub - Fingerprint segmentation")                #stub
        print("   Input - a fingerprint image")                 #stub
        print("   Output - a segmented image")                  #stub
        print("   Output - a mask image (region-of-interest)")  #stub
        segmentedImg = fpImg                                    #stub       
        maskImg = fpImg                                         #stub

        rows, cols, *ch = maskImg.shape
        total = 0
        sd = 0
        size = self.blockSize**2


        for row in range(0,rows,self.blockSize):
            for col in range(0,cols,self.blockSize):
                try:
                    gx = cv2.Sobel(fpImg[row:row+self.blockSize, col:col+self.blockSize], cv2.CV_32F, 1, 0)
                    gy = cv2.Sobel(fpImg[row:row+self.blockSize, col:col+self.blockSize], cv2.CV_32F, 0, 1)
                    absGx = cv2.convertScaleAbs(gx)
                    absGy = cv2.convertScaleAbs(gy)
                    meanx,stdx = cv2.meanStdDev(absGx)
                    meany,stdy = cv2.meanStdDev(absGy)
                    if(stdx+stdy < 150):
                        for r in range(row,row+self.blockSize):
                            for c in range(col,col+self.blockSize):
                                segmentedImg[r,c] = 0
                    
                except Exception:
                    pass     
        
        return segmentedImg, maskImg

   
#-----------------------------

if __name__ == "__main__":
    
    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    segmentator = FpSegmentator(16)
    segmentedImg,maskImg = segmentator.segment(img)
    cv2.imshow("maskImg", maskImg)
    cv2.imshow("segment", segmentedImg)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
