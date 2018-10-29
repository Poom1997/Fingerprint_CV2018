import cv2
import numpy as np
import FpSegmentator
import FpEnhancer
import MnExtractor
import MnMatcher
#iceyo try--------------------
import Binarizer
import Skeletonizer

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
    #read fingerprint image 1
##    fpImg1 = cv2.imread("../FP DB1 (train subset)/1_1.bmp", cv2.IMREAD_GRAYSCALE)
##    cv2.imshow("fp1", fpImg1);
##
##    #read fingerprint image 2
##    fpImg2 = cv2.imread("../FP DB1 (train subset)/1_2.bmp", cv2.IMREAD_GRAYSCALE)
##    cv2.imshow("fp2", fpImg2);
##
##    #match two fingerprint images
##    fpMatcher = FpMatcher()
##    similarity = fpMatcher.match(fpImg1, fpImg2)
##    print("Similary = ", similarity)
#-----------------------------
    ##Iceyo try code---------------------------------------
    img = cv2.imread("img/1_3.bmp", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("img", img)
    segmentator = FpSegmentator.FpSegmentator(16)
    segmentedImg,maskImg = segmentator.segment(img)
    cv2.imshow("segment", segmentedImg)

    binImg = Binarizer.Binarizer.binarize(segmentedImg)
    cv2.imshow("binary", binImg)

    inverseSegmentImg = segmentator.inverseSegment(binImg)
    cv2.imshow("inverseSegmentImg", inverseSegmentImg)

    skeletonizer = Skeletonizer.Skeletonizer()
    skeletonizeImg = skeletonizer.skeletonize(inverseSegmentImg)
    cv2.imshow("skeletonizeImg", skeletonizeImg)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
#-----------------------------
