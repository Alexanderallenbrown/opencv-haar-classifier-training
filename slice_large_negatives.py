import cv2
from numpy import *
import os

path = os.getcwd()
files = os.listdir(path)
i=1
k=1#index keeping track of which sub-image we're looking at.

for file in files:
    print file[-4:-1]
    if file[-4:-1]=='.pn':
        
        os.rename(os.path.join(path, file), os.path.join(path, str(i)+'_'+str(k)+'.png'))
        i = i+1
