import cv2
import numpy as np
import FpSegmentator
from OfDetector import OfDetector
from GaborFilterbank import *
from Binarizer import *

#-----------------------------
class FpEnhancer:
    def enhance(self, fpImg, mskImg):
      print("Stub - Fingerprint Enhancement")                 #stub
      print("   Input - a fingerprint image (gray-scale)")    #stub
      print("   Input - a mask image (region-of-interest)")   #stub
      print("   Output - an enhanced image")                  #stub

      # Call OfDetector

      ofDetector = OfDetector()
      orientationField = ofDetector.detect(fpImg)

      gbfb = GaborFilterbank()
      gbfb.filter(fpImg, orientationField, None)


      enhImg = fpImg                                          #stub
      return enhImg
        
###-----------------------------
if __name__ == "__main__":
    ##pass
    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    fpEnhancer = FpEnhancer()
    binImg = Binarizer.binarize(img)
    blur = cv2.bilateralFilter(binImg,11,115,115)
    cv2.imshow("blur", blur)
    img = fpEnhancer.enhance(blur, img)



    # binImg = Binarizer.binarize(img)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------

