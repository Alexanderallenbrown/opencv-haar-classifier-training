import os
import cv2

path = os.getcwd()
files = os.listdir(path)
i=1

for file in files:
    print file[-4:-1]
    if file[-4:-1]=='.pn':
        os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.png'))
        i = i+1
    elif file[-4:-1]=='.jp':

        im = cv2.imread(file)
        cv2.imwrite(str(i) + '.png', im)
        i=i+1