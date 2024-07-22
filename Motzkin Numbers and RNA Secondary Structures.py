# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:01:48 2024

@author: gbulb
"""

class Motzkin_Numbers_and_RNA_Secondary_Structures:
   def Motzkin_Numbers(k):
        if(k>2):
          result = k+Motzkin_Numbers_and_RNA_Secondary_Structures.Motzkin_Numbers(k-1)-1
        elif k==0 or k==1:
          result = 1
        elif k==2:
          result = 2
        return result
if __name__ == "__main__":    
  print(Motzkin_Numbers_and_RNA_Secondary_Structures.Motzkin_Numbers(4))