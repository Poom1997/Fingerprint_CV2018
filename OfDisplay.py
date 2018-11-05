import cv2
import numpy as np
import OfDetector
import FpEnhancer

#-----------------------------
class OfDisplay:
    def displayOrient(self, ofMat, img):
        print("Stub - Construct Orientation Field Image")   #stub
        print("   Input - a Orientation Matrix")            #stub
        print("   Output - Orientation Field Image")        #stub

        
        of = ofMat

        for rows in range(0,16):
            for cols in range(0,16):
                of[rows, cols] = 180 - of[rows, cols]

        ofImg = np.zeros((256,256), dtype=np.float32)
        ofImg[:] = 255

        rows, cols = ofImg.shape
        #print(ofMat)
        for row in range(0,rows,16):
            for col in range(0,cols,16):
                if(np.mean(img[row:row+16, col:col+16]) == 255):
                    continue
                if(of[row//16,col//16] == 0 or of[row//16,col//16] == 180):
                    cv2.line(ofImg,(col+2,row+8),(col+16-2,row+8),0,1)            
                elif(of[row//16,col//16] == 22.5):
                    cv2.line(ofImg,(col-2,row+16-2),(col+16-2,row+8+2),0,1)
                elif(of[row//16,col//16] == 45):
                    cv2.line(ofImg,(col-2,row+16-2),(col+16-2,row+2),0,1)
                elif(of[row//16,col//16] == 67.5):
                    cv2.line(ofImg,(col+4+2,row+16-2),(col+12-2,row+2),0,1)
                elif(of[row//16,col//16] == 90):
                    cv2.line(ofImg,(col+8,row+2),(col+8,row+16-2),0,1)
                elif(of[row//16,col//16] == 112.5):
                    cv2.line(ofImg,(col+16-2,row+16-2),(col+4+2,row+2),0,1)
                elif(of[row//16,col//16] == 135.0):
                    cv2.line(ofImg,(col+16-2,row+16-2),(col+2,row+2),0,1)
                elif(of[row//16,col//16] == 157.5):
                    cv2.line(ofImg,(col+16-2,row+16-2),(col+2,row+8+2),0,1)
                elif(of[row//16,col//16] == 157.5):
                    pass
                
        #cv2.imshow("ofImg", ofImg)

        
        return ofImg
        
#-----------------------------
if __name__ == "__main__":
    pass
##    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
##    cv2.imshow("input image", img)
##    fpEnhancer = FpEnhancer.FpEnhancer()
##    ofDisplay = OfDisplay()
##    blur = cv2.bilateralFilter(img,11,100,100)
##    enhancedImg = fpEnhancer.enhance(blur, blur)
##    cv2.imshow("Enhanced", enhancedImg)
##    ofMat = fpEnhancer.getOfMatrix()
##    ofDisplay.displayOrient(ofMat)
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------
