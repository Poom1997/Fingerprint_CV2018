import cv2
import numpy as np
import FpSegmentator
from OfDetector import OfDetector
from GaborFilterbank import *
from Binarizer import *

class FpEnhancer:
    def __init__(self):
        self.ofMat = []
        self.original = []
        
    def enhance(self, fpImg, mskImg):
      print("Stub - Fingerprint Enhancement")
      print("   Input - a fingerprint image (gray-scale)")
      print("   Input - a mask image (region-of-interest)")
      print("   Output - an enhanced image")

      # Call OfDetector
      ofDetector = OfDetector()
      orientationField, orientationMatrix,originalData = ofDetector.detect(fpImg)
      self.ofMat = orientationMatrix
      self.original = originalData

      gbfb = GaborFilterbank()
      enhImg = gbfb.filter(fpImg, orientationField, None)

      return enhImg

    def getOfMatrix(self):
        return self.ofMat

    def getOrientation(self, x, y):
        row = x // 16
        col = y // 16
        return self.original[row, col]

