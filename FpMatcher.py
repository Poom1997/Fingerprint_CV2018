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

    #show of
##    ofImg = inverseSegmentImg.copy()
##    ofImg[:,:] = 255
##    OfDetector = OfDetector.OfDetector()
##    of = OfDetector.getOrientation(inverseSegmentImg.copy())
    

##    ofImg = inverseSegmentImg.copy()
##    ofImg[:,:] = 255
##    OfDetector = OfDetector.OfDetector()
##    of = OfDetector.detect(inverseSegmentImg.copy())
##    
##    rows, cols, *ch = inverseSegmentImg.shape
##    for row in range(0,rows,16):
##        for col in range(0,cols,16):
##            if(of[row//16,col//16] == 0 or of[row//16,col//16] == 180):
##                cv2.line(ofImg,(col,row+8),(col+16,row+8),0,1)            
##            elif(of[row//16,col//16] == 22.5):
##                cv2.line(ofImg,(col,row+16),(col+16,row+8),0,1)
##            elif(of[row//16,col//16] == 45):
##                cv2.line(ofImg,(col,row+16),(col+16,row),0,1)
##            elif(of[row//16,col//16] == 67.5):
##                cv2.line(ofImg,(col,row+16),(col+8,row),0,1)
##            elif(of[row//16,col//16] == 90):
##                cv2.line(ofImg,(col+8,row),(col+8,row+16),0,1)
##            elif(of[row//16,col//16] == 112.5):
##                cv2.line(ofImg,(col+16,row+16),(col+8,row),0,1)
##            elif(of[row//16,col//16] == 135.0):
##                cv2.line(ofImg,(col+16,row+16),(col,row),0,1)
##            elif(of[row//16,col//16] == 157.5):
##                cv2.line(ofImg,(col+16,row+16),(col,row+8),0,1)
##            elif(of[row//16,col//16] == 157.5):
##                pass
##    cv2.imshow("ofImg", ofImg)
##    of2 = OfDetector.compute_real_orientation(inverseSegmentImg.copy())
                

    #thin
    skeletonizer = Skeletonizer.Skeletonizer()
    skeletonizeImg = skeletonizer.skeletonize(inverseSegmentImg)
    cv2.imshow("Skeletonized", skeletonizeImg)

    #extract
    minutiaImg = skeletonizeImg.copy()
    mnExtractor = MnExtractor.MnExtractor()
    ridge_ending_list,bifurcation_list = mnExtractor.extract(skeletonizeImg)
    minutiaImg = cv2.cvtColor(minutiaImg,cv2.COLOR_GRAY2BGR)
    rows, cols, *ch = minutiaImg.shape
    for row in range(1,rows-1):
        for col in range(1,cols-1):
            if((row,col) in bifurcation_list):
                minutiaImg[row-1:row+2,col-1:col+2] = [0,0,255]
            elif((row,col) in ridge_ending_list):
                minutiaImg[row-1:row+2,col-1:col+2] = [255,0,0]
    cv2.imshow("Minutia", minutiaImg)
                
    
    cv2.waitKey()
    cv2.destroyAllWindows()
#-----------------------------
