import cv2
import numpy as np
import Binarizer
import Skeletonizer

#-----------------------------
#minutiae types
M_TYPE_UNKNOWN      = 0
M_TYPE_ENDPOINT     = 1
M_TYPE_BIFURCATION  = 2
#-----------------------------
class MnExtractor:
    def __init__(self):
        #constructing Binarizer
        #constructing Skeletonizer
        self.a = 5
        
    def extract(self,enhancedImg):
        print("Stub - Minutia Extraction")                      #stub
        print("   Input - an enhanced fingerprint image")       #stub
        print("   Output - a set of minutiae")                  #stub
##        mnSet = [[ 10,  25, M_TYPE_ENDPOINT], \
##                 [120,  78, M_TYPE_BIFURCATION], \
##                 [104, 125, M_TYPE_BIFURCATION]]    #stub       
##        return mnSet
        #iceyo try code

        bifurcation_list = []
        ridge_ending_list = []
        minutia_count = 0
        
        minutiaImg = enhancedImg.copy()                #stub
        rows, cols, *ch = minutiaImg.shape
        for row in range(1,rows-1):
            for col in range(1,cols-1):
                if(minutiaImg[row,col] == 0):
                    cn = self.calculateCn(minutiaImg[row-1:row+2,col-1:col+2].copy())
                    if(cn == 1):
                        ridge_ending_list.append((row,col))
                    elif(cn == 3):
                        bifurcation_list.append((row,col))
        return ridge_ending_list,bifurcation_list
            

    def calculateCn(self,mat):
        Sum = 0
        lt = [mat[0,0], mat[0,1],mat[0,2],mat[1,2],mat[2,2],mat[2,1],mat[2,0],mat[1,0]]
        for i in range(0,len(lt)-1):
            Sum += abs((lt[i]/255) - (lt[i+1]/255))
        Sum += abs((lt[-1]/255)  - (lt[0]/255))
        return 0.5 * Sum
            
              
#-----------------------------
if __name__ == "__main__":
    pass
##    img = cv2.imread("img/1_1.bmp", cv2.IMREAD_GRAYSCALE)
##    mnSet = MnExtractor.extract(img)
##    print(mnSet)
##    print(len(mnSet))
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------
