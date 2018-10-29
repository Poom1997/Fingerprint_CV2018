import cv2
import numpy as np

#-----------------------------
class Skeletonizer:
    def skeletonize(self, binImg):
        print("Stub - Skeletonization")         #stub
        print("   Input - a binary image")      #stub
        print("   Output - a skeleton image")   #stub
        skeletonImg = binImg.copy()                #stub

        rows, cols, *ch = binImg.shape
        deleting = True
        Round = 0
        while(deleting):
            Round += 1
            deleting = False
            for row in range(1,rows-1):
                for col in range(1,cols-1):
                    if(skeletonImg[row,col] == 0):
                        if(self.countWhiteToBlack(skeletonImg[row-1:row+2,col-1:col+2].copy()) == 1):
                            count = self.countBlack(skeletonImg[row-1:row+2,col-1:col+2].copy())
                            if(count >= 2 and count <= 6):
##                                if(self.checkCondition(skeletonImg[row-1:row+2,col-1:col+2].copy())):
##                                    skeletonImg[row,col] = 255
##                                    deleting = True
                                if(Round % 2 == 0 and self.checkOddCondition(skeletonImg[row-1:row+2,col-1:col+2])):
                                    skeletonImg[row,col] = 255
                                    deleting = True
                                elif(Round % 2 != 0 and self.checkEvenCondition(skeletonImg[row-1:row+2,col-1:col+2])):
                                    skeletonImg[row,col] = 255
                                    deleting = True
                                
        return skeletonImg

    def checkCondition(self,mat):
        return mat[1,2] == 255 or mat[2,1] == 255 or (mat[0,1] == 255 and mat[1,0] == 255)

    def checkOddCondition(self, mat):
        if(mat[0,1] == 255 or mat[1,2] == 255 or mat[2,1] == 255):
            return True
        if(mat[1,2] == 255 or mat[2,1] == 255 or mat[1,0] == 255):
            return True
        return False

    def checkEvenCondition(self, mat):
        if(mat[0,1] == 255 or mat[1,2] == 255 or mat[1,0] == 255):
            return True
        if(mat[0,1] == 255 or mat[2,1] == 255 or mat[1,0] == 255):
            return True
        return False

    def countBlack(self, mat):
        count = 0
        lt = [mat[0,0], mat[0,1],mat[0,2],mat[1,2],mat[2,2],mat[2,1],mat[2,0],mat[1,0]]
        for i in range(0,len(lt)):
            if(lt[i] == 0):
                count += 1
        return count

    def countWhiteToBlack(self, mat):
        count = 0
        lt = [mat[0,0], mat[0,1],mat[0,2],mat[1,2],mat[2,2],mat[2,1],mat[2,0],mat[1,0]]
        for i in range(0,len(lt)-1):
            if(lt[i] == 255 and lt[i+1] == 0):
                count += 1
        if(lt[-1] == 255 and lt[0] == 0):
            count += 1
        return count
    
#-----------------------------
##if __name__ == "__main__":
##    img = cv2.imread("1_1.bmp", cv2.IMREAD_GRAYSCALE)
##    from Binarizer import Binarizer
##    binImg = Binarizer.binarize(img)
##    skeletonImg = Skeletonizer.skeletonize(binImg)
##    cv2.imshow("skeleton", skeletonImg)
##    cv2.imwrite("skeleton.bmp", skeletonImg)
##    cv2.waitKey()
##    cv2.destroyAllWindows()

#-----------------------------

