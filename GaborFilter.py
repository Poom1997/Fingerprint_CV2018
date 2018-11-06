import cv2
import numpy as np

class GaborFilter:
    def __init__(self, size, orientation, frequency):
        self.size = size
        self.orientation = orientation
        self.frequency = frequency

    def getKernal(self):
        kernel = cv2.getGaborKernel(self.size, 3, self.orientation*np.pi/180, self.frequency, 4, 0, cv2.CV_32F)
        
        return kernel
