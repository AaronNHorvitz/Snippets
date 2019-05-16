# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:19:03 2019

@author: ahorvitz
"""
"""
This little snippet of code, renames all the files in one directory and deposits them in another directory.
The new filename is the right most ten characters. 
"""

import os

baseDirectory = "C:/Source"          #Location of the files to truncate
newDirectory  = "C:/Deposit"         #Location of the files after they have been truncated

count = 0
for oldFileName in os.listdir(baseDirectory):

    newFileName = oldFileName[-10:]    #This takes the right most 10 characters in the file.
    newFileName = os.path.join(newDirectory,newFileName)
    
    if not os.path.isfile(newFileName):
        count += 1
        print(count," ",newFileName)
        os.rename(os.path.join(baseDirectory, oldFileName), newFileName)
    else: 
        count += 1
        print(count, " File already exists: " + newFileName)
