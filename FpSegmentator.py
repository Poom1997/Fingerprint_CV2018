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

##        for row in range(0,rows,self.blockSize):
##            for col in range(0,cols,self.blockSize):
##                try:
##                    for r in range(row,row+16):
##                        for c in range(col,col+16):
##                            total += maskImg[r,c]
##                    for r in range(row,row+16):
##                        for c in range(col,col+16):
##                            sd += (maskImg[r,c] - (total//size))**2
##                    sd = math.sqrt(sd//self.blockSize)
##                    if(total//size > 200 or total//size < 75) and sd < 150:
##                        for r in range(row,row+16):
##                            for c in range(col,col+16):
##                                segmentedImg[r,c] = 0
##                                
##                    total = 0
##                    sd = 0
##                       
##                except Exception:
##                    pass
                    
        
        return segmentedImg, maskImg

   
#-----------------------------

if __name__ == "__main__":
    img = cv2.imread("Images/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    segmentator = FpSegmentator(16)
    segmentedImg,maskImg = segmentator.segment(img)
    cv2.imshow("segment", segmentedImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
