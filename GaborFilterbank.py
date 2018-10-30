import cv2
import numpy as np
import GaborFilter
import math


# -----------------------------
class GaborFilterbank:
    def __init__(self):
        print("Stub - Constructing Gabor filterbank")  # stub

        gaborFilters = []

        for radian in np.arange(0, np.pi, np.pi / 8):
            degree = math.degrees(radian)

            gb = GaborFilter.GaborFilter((9, 9), degree, 50)
            gaborFilters.append(gb.getKernal())

        # gaborFilters = ...                       #list of Gabor filters

    def filter(self, fpImg, ofImg, mskImg):
        print("Stub - Gabor filtering")  # stub

        print("   Input - a fingerprint image (gray-scale)")  # stub
        cv2.imread('img/1_1.BMP', cv2.GRAYSCALE)

        print("   Input - an orientation field")  # stub

        print("   Input - a mask image (region-of-interest)")  # stub
        
        print("   Output - a filtered image")  # stub
        filteredImg = fpImg  # stub
        return filteredImg  # stub


# -----------------------------
if __name__ == "__main__":
    gBank = GaborFilterbank()

# -----------------------------
