import cv2
import numpy as np

class Binarizer:
    def binarize(fpImg):
        retval, binImg = cv2.threshold(fpImg, 0, 255, \
                                cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        return binImg
        
