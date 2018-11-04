import cv2
import numpy as np
import GaborFilter
import math

# -----------------------------
class GaborFilterbank:
    def __init__(self):
        print("Stub - Constructing Gabor filterbank")  # stub
        self.gaborFilters = {}
        orList = [0, 22.5,45,67.5,90,112.5,135,157.5,180]
        for degree in orList:
            gb = GaborFilter.GaborFilter((16, 16), degree, 8)
            #self.gaborFilters.append(gb.getKernal())
            self.gaborFilters[degree] = gb.getKernal()

        #print(self.gaborFilters)

    def filter(self, fpImg, orientationField, mskImg):
        fpImg = np.float32(fpImg)
        cv2.imshow('filted by gabor', fpImg)
        #print(orientationField)
        print("Stub - Gabor filtering")  # stub
        print("   Input - a fingerprint image (gray-scale)")  # stub
        #filtered_img = cv2.filter2D(fpImg, cv2.CV_8UC3, self.gaborFilters[22.5])

        ## >> Need help <<
        rows, cols = fpImg.shape
        for row in range(0, rows, 16):
            for col in range(0, cols, 16):
                block = fpImg[row: row+16, col: col+16]
                orientationOfBlock = orientationField[row//16][col//16]
                print(orientationOfBlock, end=' ')
                filteredBlock = cv2.filter2D(block, cv2.CV_32F, self.gaborFilters[orientationOfBlock])
                fpImg[row: row+16, col: col+16] = filteredBlock
            print()

        cv2.imshow('filted by gabor', fpImg)

        print("   Input - an orientation field")  # stub
        print("   Input - a mask image (region-of-interest)")  # stub
        print("   Output - a filtered image")  # stub
        # filteredImg = fpImg  # stub
        return None  # stub

# -----------------------------
if __name__ == "__main__":
    pass
##    gBank = GaborFilterbank()
##
##    fpImg = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
##    gBank.filter(fpImg,1,1)
##    cv2.waitKey(0)

# -----------------------------
