import cv2
import numpy as np
import OfDetector
import FpEnhancer

class OfDisplay:
    def displayOrient(self, ofMat, img):
        of = ofMat
        for rows in range(0,16):
            for cols in range(0,16):
                of[rows, cols] = 180 - of[rows, cols]

        ofImg = np.zeros((256,256), dtype=np.float32)
        ofImg[:] = 255

        rows, cols = ofImg.shape
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

        return ofImg
