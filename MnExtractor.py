import cv2
import numpy as np
import Binarizer
import Skeletonizer
#iceyo try import
import math

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
                    if(cn == 1 and (not self.isEndPointBoundary(minutiaImg,(row,col)))):
                        ridge_ending_list.append((row,col))
                    elif(cn == 3):
                        bifurcation_list.append((row,col))
        return ridge_ending_list,bifurcation_list

    def removeSideMinutia(self, img,minutia_list):
        useable_mn = []
        for mn in minutia_list:
            center = (mn[0] - mn[0]%16,mn[1] - mn[1]%16)
            if(np.mean(img[center[0] : center[0]+16, center[1]-16:center[1]]) == 255):
                continue
            elif(np.mean(img[center[0] : center[0]+16, center[1]+16:center[1]+32]) == 255):
                continue
            else:
                useable_mn.append(mn)
        return useable_mn
                
    def removeBrokenRidge(self,minutia_list):
        optimal_end_ridge = minutia_list.copy()
        
        for i in range(0,len(minutia_list)):
            for j in range(0,len(minutia_list)):
                if(minutia_list[i] != minutia_list[j]):
                    if(math.sqrt(((minutia_list[i][0] - minutia_list[j][0])**2) + ((minutia_list[i][1] - minutia_list[j][1])**2)) < 5):
                        try:
                            optimal_end_ridge.remove(minutia_list[i])
                        except Exception:
                            pass
                        try:
                            optimal_end_ridge.remove(minutia_list[j])
                        except Exception:
                            pass
        return optimal_end_ridge

    def isEndPointBoundary(self,mat,point):
        isBoundary = True
        rows, cols, *ch = mat.shape
        for col in range(point[1]-1, 0,-1):
            if(mat[point[0], col] == 0):
                isBoundary = False
                break

        if(isBoundary == True):
            return isBoundary
        
        isBoundary = True
        for col in range(point[1]+1, cols):
            if(mat[point[0], col] == 0):
                isBoundary = False
                break

        return isBoundary
                
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
