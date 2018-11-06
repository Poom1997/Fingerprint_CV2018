import cv2
import numpy as np
import FpSegmentator
import FpEnhancer
import MnExtractor
import MnMatcher
import Binarizer
import Skeletonizer
import OfDetector
import OfDisplay

#-----------------------------
class FpMatcher:
    def __init__(self):
        pass

    def getMinutia(self, fpImg):
        img = fpImg

        #segment1
        segmentator = FpSegmentator.FpSegmentator(16)
        segmentedImg,maskImg = segmentator.segment(img)

        #binarize
        binImg = Binarizer.Binarizer.binarize(segmentedImg)

        #segment2
        inverseSegmentImg = segmentator.inverseSegment(binImg)

        #enhance
        fpEnhancer = FpEnhancer.FpEnhancer()
        blur = cv2.bilateralFilter(inverseSegmentImg,11,100,100)
        enhancedImg = fpEnhancer.enhance(blur, inverseSegmentImg)
        rows, cols, *ch = maskImg.shape
        for row in range(0,rows):
            for col in range(0,cols):
                if(enhancedImg[row,col] != 0):
                    enhancedImg[row,col] = 255

        #thin
        skeletonizer = Skeletonizer.Skeletonizer()
        skeletonizeImg = skeletonizer.skeletonize(enhancedImg)

        #extract
        minutiaImg = skeletonizeImg.copy()
        mnExtractor = MnExtractor.MnExtractor()
        ridge_ending_list,bifurcation_list = mnExtractor.extract(skeletonizeImg)
        
        ridge_ending_list = mnExtractor.removeSideMinutia(skeletonizeImg,ridge_ending_list)
        ridge_ending_list = mnExtractor.removeBrokenRidge(ridge_ending_list)
        bifurcation_list = mnExtractor.removeSideMinutia(skeletonizeImg,bifurcation_list)
        bifurcation_list = mnExtractor.removeBrokenRidge(bifurcation_list)
     
        minutia_list = list(set(ridge_ending_list + bifurcation_list))
        minutia_list = mnExtractor.removeBrokenRidge(minutia_list)

        minutiaImg = cv2.cvtColor(minutiaImg,cv2.COLOR_GRAY2BGR)
        minutiaImg2 = minutiaImg.copy()
        rows, cols, *ch = minutiaImg.shape
        for row in range(1,rows-1):
            for col in range(1,cols-1):
                if((row,col) in bifurcation_list):
                    minutiaImg[row-1:row+2,col-1:col+2] = [0,0,255]
                elif((row,col) in ridge_ending_list):
                    minutiaImg[row-1:row+2,col-1:col+2] = [255,0,0]


        test_lt = [(91, 164),(29, 106)]
        test_lt2 = [(82, 169),(20, 113)]
        for row in range(1,rows-1):
            for col in range(1,cols-1):
                if((row,col) in test_lt):
                    minutiaImg2[row-1:row+2,col-1:col+2] = [255,0,0]
                elif((row,col) in test_lt2):
                    minutiaImg2[row-1:row+2,col-1:col+2] = [0,0,255]

        return minutia_list
    
    def match(self, fpImg1, fpImg2):
        minutia1 = self.getMinutia(fpImg1)
        minutia2 = self.getMinutia(fpImg2)
        matcher = MnMatcher.MnMatcher()
        similarity = matcher.match(minutia1, minutia2)
        return similarity
