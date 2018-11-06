import cv2
import numpy as np
import GaborFilter
import math

class GaborFilterbank:
    def __init__(self):
        self.gaborFilters = {}
        orList = [0, 22.5,45,67.5,90,112.5,135,157.5,180]
        for degree in orList:
            gb = GaborFilter.GaborFilter((11,11), degree, 8)
            self.gaborFilters[degree] = gb.getKernal()


    def filter(self, fpImg, orientationField, mskImg):
        fpImg = np.float32(fpImg)
        rows, cols = fpImg.shape
        for row in range(0, rows, 16):
            for col in range(0, cols, 16):
                block = fpImg[row: row+16, col: col+16]
                orientationOfBlock = orientationField[row//16][col//16]
                filteredBlock = cv2.filter2D(block, cv2.CV_8UC3, self.gaborFilters[orientationOfBlock])
                fpImg[row: row+16, col: col+16] = filteredBlock

        return fpImg

