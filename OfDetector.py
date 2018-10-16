import cv2
import numpy as np

#-----------------------------
class OfDetector:
    def __init__(self):
        pass
    
    def detect(self, fpImg, mskImg):
        
        height, width = fpImg.shape
        
        ofMat = fpImg
        ofImg = fpImg
        return ofMat, ofImg
        
#-----------------------------
if __name__ == "__main__":
    inpImg = cv2.imread("img/1_1.BMP", cv2.IMREAD_GRAYSCALE)
    ofDetect = OfDetector()
    outMat, outImg = ofDetect.detect(inpImg, inpImg)
    cv2.imshow("input", inpImg)
    cv2.imshow("Output", inpImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------


