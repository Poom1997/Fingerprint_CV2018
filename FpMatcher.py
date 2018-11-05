import cv2
import numpy as np
import FpSegmentator
import FpEnhancer
import MnExtractor
import MnMatcher
#iceyo try--------------------
import Binarizer
import Skeletonizer
import OfDetector

#-----------------------------
class FpMatcher:
    def __init__(self):
        #constructing FpSegmentator
        
        #constructing FpEnhancer
        
        #constructing MnExtractor
        
        #constructing MnMatcher
        pass
        
    def match(self, fpImg1, fpImg2):
        print("Stub - Fingerprint Matching")                #stub
        print("   Input - a fingerprint image (template)")  #stub
        print("   Input - a fingerprint image (input)")     #stub
        print("   Output - similarity score")               #stub
        similarity = 0.75                                   #stub
        return similarity                                   #stub
        
#-----------------------------

if __name__ == "__main__":
    ##Iceyo try code---------------------------------------
    
    img = cv2.imread("img/1_3.bmp", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Original Image", img)

    #segment1
    segmentator = FpSegmentator.FpSegmentator(16)
    segmentedImg,maskImg = segmentator.segment(img)
    cv2.imshow("Segmented", segmentedImg)

    #binarize
    binImg = Binarizer.Binarizer.binarize(segmentedImg)
    cv2.imshow("Binarize", binImg)

    #segment2
    inverseSegmentImg = segmentator.inverseSegment(binImg)
    cv2.imshow("InverseSegmented", inverseSegmentImg)

    #enhance
    fpEnhancer = FpEnhancer.FpEnhancer()
    blur = cv2.bilateralFilter(inverseSegmentImg,11,100,100)
    enhancedImg = fpEnhancer.enhance(blur, inverseSegmentImg)
    cv2.imshow("Enhanced", enhancedImg)
    

##    #binarize again
##    binImg = Binarizer.Binarizer.binarize(enhancedImg)
##    cv2.imshow("Binarize2", binImg)
##
##    #thin
##    skeletonizer = Skeletonizer.Skeletonizer()
##    skeletonizeImg = skeletonizer.skeletonize(binImg)
##    cv2.imshow("Skeletonized", skeletonizeImg)
##
##    #extract
##    minutiaImg = skeletonizeImg.copy()
##    mnExtractor = MnExtractor.MnExtractor()
##    ridge_ending_list,bifurcation_list = mnExtractor.extract(skeletonizeImg)
##    minutiaImg = cv2.cvtColor(minutiaImg,cv2.COLOR_GRAY2BGR)
##    rows, cols, *ch = minutiaImg.shape
##    for row in range(1,rows-1):
##        for col in range(1,cols-1):
##            if((row,col) in bifurcation_list):
##                minutiaImg[row-1:row+2,col-1:col+2] = [0,0,255]
##            elif((row,col) in ridge_ending_list):
##                minutiaImg[row-1:row+2,col-1:col+2] = [255,0,0]
##    cv2.imshow("Minutia", minutiaImg)
                
    
    cv2.waitKey()
    cv2.destroyAllWindows()
#-----------------------------
