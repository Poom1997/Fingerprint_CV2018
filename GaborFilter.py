import cv2
import numpy as np

# -----------------------------


class GaborFilter:
    def __init__(self, size, orientation, frequency):
        print("Constructing a Gabor filter")  # stub
        self.size = size
        self.orientation = orientation
        self.frequency = frequency #freq = lamda

    def getKernal(self):
        kernel = cv2.getGaborKernel(
            self.size, 3 , self.orientation, self.frequency, 2, 0, ktype=cv2.CV_32F
        )
        
        return kernel

# -----------------------------
if __name__ == "__main__":

  img = cv2.imread('img/1_1.BMP', cv2.IMREAD_GRAYSCALE)
  Filter = GaborFilter((6,6),180,0)
  kernal = Filter.getKernal()

  filtered_img = cv2.filter2D(img, cv2.CV_8UC3, kernal)

  cv2.imshow('image', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

# -----------------------------
