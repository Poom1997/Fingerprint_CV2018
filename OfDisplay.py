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

        
        of = ofMat

        for rows in range(0,16):
            for cols in range(0,16):
                of[rows, cols] = 180 - of[rows, cols]

        ofImg = np.zeros((256,256), dtype=np.float32)
        ofImg[:] = 255

        rows, cols = ofImg.shape
        print(ofMat)
        for row in range(0,rows,16):
            for col in range(0,cols,16):
                if(of[row//16,col//16] == 0 or of[row//16,col//16] == 180):
                    cv2.line(ofImg,(col,row+8),(col+16,row+8),0,1)            
                elif(of[row//16,col//16] == 22.5):
                    cv2.line(ofImg,(col,row+16),(col+16,row+8),0,1)
                elif(of[row//16,col//16] == 45):
                    cv2.line(ofImg,(col,row+16),(col+16,row),0,1)
                elif(of[row//16,col//16] == 67.5):
                    cv2.line(ofImg,(col,row+16),(col+8,row),0,1)
                elif(of[row//16,col//16] == 90):
                    cv2.line(ofImg,(col+8,row),(col+8,row+16),0,1)
                elif(of[row//16,col//16] == 112.5):
                    cv2.line(ofImg,(col+16,row+16),(col+8,row),0,1)
                elif(of[row//16,col//16] == 135.0):
                    cv2.line(ofImg,(col+16,row+16),(col,row),0,1)
                elif(of[row//16,col//16] == 157.5):
                    cv2.line(ofImg,(col+16,row+16),(col,row+8),0,1)
                elif(of[row//16,col//16] == 157.5):
                    pass
                
        cv2.imshow("ofImg", ofImg)

        
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
