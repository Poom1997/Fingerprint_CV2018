import cv2
import numpy as np

#-----------------------------
class OfDetector:
    def __init__(self):
        pass
    
    def detect(self, fpImg, mskImg):
        
        height, width = fpImg.shape

        gx = cv2.Sobel(fpImg, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(fpImg, cv2.CV_32F, 0, 1)

        for row in range(0,width):
            for col in range(0,height):
                fpImg[row,col] = 0
                
        
        return fpImg, fpImg
        
#-----------------------------
if __name__ == "__main__":
    inpImg = cv2.imread("img/1_1.BMP", cv2.IMREAD_GRAYSCALE)
    ofDetect = OfDetector()
    absGx, absGy = ofDetect.detect(inpImg, inpImg)
    cv2.imshow("absGx", absGx)
    cv2.imshow("absGy", absGy)
    cv2.waitKey()
    cv2.destroyAllWindows()

#-----------------------------


