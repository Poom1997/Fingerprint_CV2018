import cv2
import numpy as np
import OfDetector
import FpEnhancer

#-----------------------------
class OfDisplay:
    def displayOrient(self, ofMat):
        print("Stub - Construct Orientation Field Image")   #stub
        print("   Input - a Orientation Matrix")            #stub
        print("   Output - Orientation Field Image")        #stub

        
        print(ofMat)

        
        return None
        
#-----------------------------
if __name__ == "__main__":
    pass
    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("input image", img)
    fpEnhancer = FpEnhancer.FpEnhancer()
    ofDisplay = OfDisplay()
    blur = cv2.bilateralFilter(img,11,100,100)
    enhancedImg = fpEnhancer.enhance(blur, blur)
    cv2.imshow("Enhanced", enhancedImg)
    ofMat = fpEnhancer.getOfMatrix()
    ofDisplay.displayOrient(ofMat)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------
