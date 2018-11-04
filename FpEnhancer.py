import cv2
import numpy as np
import FpSegmentator
import OfDetector
from GaborFilterbank import *
from Binarizer import *

#-----------------------------
class FpEnhancer:
    def enhance(self, fpImg, mskImg):
        print("Stub - Fingerprint Enhancement")                 #stub
        print("   Input - a fingerprint image (gray-scale)")    #stub
        print("   Input - a mask image (region-of-interest)")   #stub
        print("   Output - an enhanced image")                  #stub
        gbfb = GaborFilterbank()
        gbfb.filter(fpImg, fpImg, fpImg)
        enhImg = fpImg                                          #stub
        return enhImg
        
###-----------------------------
if __name__ == "__main__":
    ##pass
    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    enhancer = FpEnhancer()
    img = enhancer.enhance(img, img)
    binImg = Binarizer.binarize(img)
    cv2.imshow("binary", binImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------

