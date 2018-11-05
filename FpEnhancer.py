import cv2
import numpy as np
import FpSegmentator
from OfDetector import OfDetector
from GaborFilterbank import *
from Binarizer import *

#-----------------------------
class FpEnhancer:
    def __init__(self):
        self.ofMat = []
        self.original = []
        
    def enhance(self, fpImg, mskImg):
      print("Stub - Fingerprint Enhancement")                 #stub
      print("   Input - a fingerprint image (gray-scale)")    #stub
      print("   Input - a mask image (region-of-interest)")   #stub
      print("   Output - an enhanced image")                  #stub

      # Call OfDetector

      ofDetector = OfDetector()
      orientationField, orientationMatrix,originalData = ofDetector.detect(fpImg)
      self.ofMat = orientationMatrix
      self.original = originalData

      gbfb = GaborFilterbank()
      enhImg = gbfb.filter(fpImg, orientationField, None)

      return enhImg

    def getOfMatrix(self):
        return self.ofMat

    def getOrientation(self, x, y):
        row = x // 16
        col = y // 16
        return self.original[row, col]
        
###-----------------------------
if __name__ == "__main__":
    pass
##    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
##    fpEnhancer = FpEnhancer()
##    binImg = Binarizer.binarize(img)
##    blur = cv2.bilateralFilter(binImg,11,100,100)
##    cv2.imshow("blur", blur)
##    img = fpEnhancer.enhance(blur, img)
##    cv2.imshow("enhanced", img)
##    # binImg = Binarizer.binarize(img)
##    
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------
