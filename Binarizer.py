import cv2
import numpy as np

#-----------------------------
class Binarizer:
    def binarize(fpImg):
        print("Stub - Binarization")                            #stub
        print("   Input - a fingerprint image (gray-scale)")    #stub
        print("   Output - a binary image")                     #stub                                      #stub

        binImg = cv2.adaptiveThreshold(img, 255,adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, \
                                                thresholdType=cv2.THRESH_BINARY, blockSize=9, C=10)
        
        return binImg
        
#-----------------------------
if __name__ == "__main__":
    pass
##    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
##    cv2.imshow("img", img)
##    binImg = Binarizer.binarize(img)
##    cv2.imshow("binary", binImg)
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------
