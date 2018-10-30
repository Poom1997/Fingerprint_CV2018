import cv2
import numpy as np
import GaborFilter
import math


# -----------------------------
class GaborFilterbank:
    def __init__(self):
        print("Stub - Constructing Gabor filterbank")  # stub

        self.gaborFilters = []

        for radian in np.arange(0, np.pi, np.pi / 8):
            degree = math.degrees(radian)

            gb = GaborFilter.GaborFilter((9, 9), degree, 6)
            self.gaborFilters.append(gb.getKernal())

        # gaborFilters = ...                       #list of Gabor filters

    def filter(self, fpImg, ofImg, mskImg):
        print("Stub - Gabor filtering")  # stub

        print("   Input - a fingerprint image (gray-scale)")  # stub
        img = cv2.imread('img/1_1.BMP', cv2.IMREAD_GRAYSCALE)

        i = 0
        for gabor in self.gaborFilters:
            filtered_img = cv2.filter2D(img, cv2.CV_8UC3, gabor)
            print('eee')
            cv2.imshow('filted image' + str(i), filtered_img)
            i +=1

        print("   Input - an orientation field")  # stub

        print("   Input - a mask image (region-of-interest)")  # stub

        print("   Output - a filtered image")  # stub
        filteredImg = fpImg  # stub
        return filteredImg  # stub


# -----------------------------
if __name__ == "__main__":
    gBank = GaborFilterbank()
    gBank.filter(1,1,1)
    cv2.waitKey(0)

# -----------------------------
