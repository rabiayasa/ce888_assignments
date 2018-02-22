"""
This project created for CE888 Data Science assignments -Evolutionary Strategies for Domain Adaptation-
Author:Rabia YASA KOSTAS
Date:22/02/2018
"""
import glob
import os
from PIL import Image

#1-This part detects the whole folders in data folder
pathnames=[]
for i in os.walk('data'):
    pathnames.append(i[0])

#2-This parts find and prints all paths of images
image1=[]
for i in pathnames:
    for image_path in glob.glob(i + '\\*.jpg'):
        print(image_path)
        image1.append(image_path)


#3-This parts load the first 10 pictures in data folder and prints the last one
#We loaded only first 10 pictures because we dont use all files now. Also the whole data set quite a lot.
#in the future works we can use whole data set using these codes.
# finding images paths (step 2) creates an easy way to use whole dataset whenever wants.
img=[]
for i in range(0,10):
    img.append( Image.open(image1[i]))
img[i].show()




