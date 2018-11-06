import cv2
import numpy as np
import math
from MnExtractor import *

class MnMatcher:

    def distance(self,x1,y1,x2,y2):
        return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    
    def matching(self, m1, m2):
        corresponding = 0
        corresponded = False
        for i in range(len(m1)):
            for j in range(len(m1)):
                if((m1[i] == m1[j])):
                    continue
                if((m1[j][0] - m1[i][0]) == 0):
                    continue
                distance_a = self.distance(m1[i][0], m1[i][1], m1[j][0], m1[j][1])#x1,x2,y1,y2 -> m1
                theta_a = abs(math.degrees(math.atan((m1[j][1] - m1[i][1]) / (m1[j][0] - m1[i][0]))))
                
                for k in range(len(m2)):
                    if(self.distance(m1[i][0], m1[i][1], m2[k][0], m2[k][1]) > 16):
                        continue
                    for l in range(len(m2)):
                        if(self.distance(m1[j][0], m1[j][1], m2[l][0], m2[l][1]) > 16):
                            continue
                        if((m2[k] == m2[l])):
                            continue
                        distance_b = self.distance(m2[k][0], m2[k][1], m2[l][0], m2[l][1])#x1,x2,y1,y2 -> m2
                        if((m2[l][0] - m2[k][0]) == 0):
                            continue
                        theta_b = abs(math.degrees(math.atan((m2[l][1] - m2[k][1]) / (m2[l][0] - m2[k][0]))))
                        if((abs(distance_a - distance_b) < 3) and (abs(theta_a - theta_b) < 5)):
                            corresponded = True
                            corresponding += 1
                            break
                    if(corresponded == True):
                        break
                if(corresponded == True):
                    corresponded = False
                    break
        return corresponding
                        
  
    def match(self, m1,m2):
        matcher = MnMatcher()
        if(len(m1) > len(m2)):
            corresponding = matcher.matching(m1,m2)
            percentage = (corresponding / len(m1))
        else:
            corresponding = matcher.matching(m2,m1)
            percentage = (corresponding / len(m2))
        return percentage
